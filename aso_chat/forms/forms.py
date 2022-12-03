from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from aso_chat.models import Room

class RegisterForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta: 
        model = Room
        fields = ['name']
    
