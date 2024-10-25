from django.contrib import admin
from .models import Message,UserStatus
# Register your models here.

admin.site.register(Message)
admin.site.register(UserStatus)