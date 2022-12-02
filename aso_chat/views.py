from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms.forms import RegisterForm
from .models import Room, RoomRegistration, Message

def home(request):
     return render(request, "chat/home.html", {})

def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)

        if(registerForm.is_valid()):
            newUser = registerForm.save()
            login(request, newUser)
            return redirect('home')
    else:
        registerForm = RegisterForm()
    
    return render(request, "chat/register.html", {'form':registerForm })

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    chats = [ {"message": "ana are mere", "username": "claudiu"}]
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name, "chats": chats})

@login_required
def rooms(request):
    # we will get the chatbox name from the url
    
    rooms_registration = RoomRegistration.objects.filter(user=request.user)

    #there are two cases 
    #invited into a room and not joined
    pending_rooms = []
    #joined the room
    joined_rooms = []
    for r in rooms_registration:
        if(r.status == 'JOINED'):
            joined_rooms.append(r.room)
        else:
            pending_rooms.append(r.room)
    return render(request, "chat/roomchat.html", {"pending_rooms": pending_rooms, "joined_rooms": joined_rooms })