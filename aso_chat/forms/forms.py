from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, RadioSelect,MultipleChoiceField

from aso_chat.models import Room, RoomRegistration, Message

class RegisterForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta: 
        model = Room
        fields = ['name']

class RoomRegistrationForm(ModelForm):
    class Meta: 
        model = RoomRegistration
        fields = ['user', 'room']

class MessageForm(ModelForm): 
    class Meta: 
        model = Message
        fields = [ 'message', 'image']
