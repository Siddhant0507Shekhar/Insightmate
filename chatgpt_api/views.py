from django.shortcuts import render
from ipware import get_client_ip
from user_agents import parse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import openai, json
from django.contrib.auth import authenticate
from rest_framework.generics import get_object_or_404
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from .models import Topics, Chats, Request_information
from rest_framework.permissions import IsAuthenticated

def user_information(info):
    print("YES we are inside user_information");
    try:
        client_ip, is_routable = get_client_ip(info)
        print(client_ip, "STEP1")
        user_agent_string = info.META.get('HTTP_USER_AGENT', '')
        print(user_agent_string, "STEP2")
        user_agent = parse(user_agent_string)
        print(user_agent, "STEP3")
        # Access user agent properties
        os_family = user_agent.os.family
        print(os_family, "STEP4")
        browser_family = user_agent.browser.family
        print(browser_family, "STEP5")
        device_family = user_agent.device.family
        print(device_family, "STEP6")
        device_model = user_agent.device.model
        print(device_model,"LAST STEP")
        other_info = json.loads(info.body)
        print(other_info, "STEP7")
        data = {
            'request_headers': json.dumps({
                'user_agent_string': user_agent_string,
                'os_family': os_family,
                'browser_family': browser_family,
                'device_family': device_family,
                'device_model':device_model
            }),
            'ip_address': client_ip,
            'other_information': json.dumps(other_info)
        }
        # Save the information to the model
        request_info = Request_information.objects.create(**data)
        request_info.save()
        return True
    except Exception as e:
        return True




# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def loadchat(request):
    user_information(request)
    data = json.loads(request.body)
    token = data["refresh_token"]
    user_id = RefreshToken(token)['user_id']
    topic_name = data.get('topic_name')
    user = User.objects.get(id=user_id)
    topic = get_object_or_404(Topics, topic=topic_name, user=user)
    chats = Chats.objects.filter(topic=topic, user=user)
    chat_data = [{'chat': chat.chat, 'answer': chat.answer, 'created_at': chat.created_at} for chat in chats]
    return JsonResponse({'chats': chat_data})

# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout(request):
    arr = json.loads(request.body.decode('utf-8'))
    token = RefreshToken(arr["refresh_token"])
    token.blacklist()
    return JsonResponse({"alright":"YES"})


# @csrf_exempt
@api_view(['POST'])
def login_api_token(request):
    user_information(request)
    # Retrieve the username and password from the request's POST data
    username = request.data.get('username')
    password = request.data.get('password')
    # Authenticate the user's credentials using Django's built-in authentication system
    user = authenticate(username=username, password=password)

    # If authentication was successful, generate a JWT token and return it in the response
    if user:
        refresh = RefreshToken.for_user(user)
        response_data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }
        return Response(response_data, status=status.HTTP_200_OK)
    # If authentication failed, return an error message
    else:
        return JsonResponse({'error': 'Invalid credentials'})



# @csrf_exempt
@api_view(['POST'])
def signup(request):
    user_information(request)
    # Retrieve the username and password from the request's POST data
    username = request.data.get('username')
    password = request.data.get('password')
    user_check = get_user_model()
    user = None
    try:
        user = user_check.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user:
        return JsonResponse({'error': 'User already Exist'})
    # Create a new user with the provided username and password
    user = User.objects.create_user(username=username, password=password)

    # Generate a JWT token for the new user
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    # Return the JWT token and a success message in the response
    return Response({'token': token, 'message': 'User created and logged in successfully'})

def chatgpt(queries):
    openai.api_key = "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"
    model_engine = "gpt-3.5-turbo"
    # This specifies which GPT model to use, as there are several models available, each with different capabilities and performance characteristics.
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": queries},
        ])

    message = response.choices[0]['message']
    return message['content']

# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def get_topics(request):
    token = json.loads(request.body.decode('utf-8'))["refresh_token"]
    user_id = RefreshToken(token)['user_id']
    if user_id is None:
        return JsonResponse(status=400)
    user = User.objects.get(id=user_id)
    topics = Topics.objects.filter(user=user).values_list('topic', flat=True)
    response = {
        'topics': list(topics)[::-1]
    }
    return JsonResponse(response, status=200)


# Create your views here.
@csrf_exempt
def response_query(request):
    user_information(request)
    if request.method=="POST":
        data = json.loads(request.body)
        query = data.get('query')
        opt = chatgpt(query)
        ret = {"Assistant": opt}
        if data.get("refresh_token") is not None:
            token = data["refresh_token"]
            user_id = RefreshToken(token)['user_id']
            topic = data["topic"]
            if (topic=="") or topic is None:
                get_topic_name = "Can u please get the following line a suitable topic of 2-5 words?   "+query
                topic = chatgpt(get_topic_name.strip('"'))
                ret["newTopic"] = True
                ret["newTopicname"] = topic
            user = User.objects.get(id=user_id)
            topic_obj, _ = Topics.objects.get_or_create(user=user, topic=topic)
            chat = Chats(chat=query, answer=opt, user=user, topic=topic_obj, created_at=timezone.now())
            chat.save()
        return JsonResponse(ret,status=200)
    else:
        return JsonResponse({"error":"Wrong HTTP method"},status=500)
