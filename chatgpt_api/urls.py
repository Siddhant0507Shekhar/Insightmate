from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('response_query',views.response_query,name='response_query' ),
    path('signup',views.signup,name='signup'),
    path('login',views.login_api_token,name="login_token"),
    path('logout',views.logout,name='logout'),
    path('topics',views.get_topics,name='logout'),
    path('loadchat',views.loadchat,name='logout'),
]
