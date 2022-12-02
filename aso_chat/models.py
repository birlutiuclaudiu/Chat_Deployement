from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save


# Create your models here.

class Room(models.Model):
    created_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True, blank="False")
    slug = models.SlugField(max_length = 250, null = False, unique=True, blank = False)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    message = models.CharField(max_length=1000,blank=False)
    published_at = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ('published_at',)

class RoomRegistration(models.Model):
    status = models.CharField(max_length=10, unique=False, blank="False")
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, blank=False, on_delete=models.CASCADE)


@receiver(pre_save, sender=Room)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
