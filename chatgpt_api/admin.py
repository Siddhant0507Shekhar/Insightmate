from django.contrib import admin
from .models import Topics, Chats, Request_information
# Register your models here.
admin.register(Topics)
admin.site.register(Topics)

admin.register(Request_information)
admin.site.register(Request_information)

admin.register(Chats)
admin.site.register(Chats)


