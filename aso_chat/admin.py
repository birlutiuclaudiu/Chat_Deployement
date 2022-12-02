from django.contrib import admin
# Register your models here.
from .models import Room, Message, RoomRegistration

admin.site.register([Room, Message,RoomRegistration])