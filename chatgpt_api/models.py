# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Topics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Chats(models.Model):
    chat = models.TextField()
    answer = models.TextField(default="dummy")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Request_information(models.Model):
    request_headers = models.TextField(default="NOTHING")
    ip_address = models.TextField(default=">>>")
    other_information = models.TextField(default="NOTHING")


