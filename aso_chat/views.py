from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms.forms import RegisterForm, RoomForm, RoomRegistrationForm
from .models import Room, RoomRegistration, Message

def home(request):
     return render(request, "chat/home.html", {})

def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)

        if(registerForm.is_valid()):
            newUser = registerForm.save()
            login(request, newUser)
            return redirect('rooms')
    else:
        registerForm = RegisterForm()
    
    return render(request, "chat/register.html", {'form':registerForm })

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    chats = [ {"message": "ana are mere", "username": "claudiu"}]
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name, "chats": chats})

@login_required
def rooms(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        
        if form.is_valid():
            room  = form.save(commit=False)
            room.created_by = request.user
            room.save()
            return redirect('rooms')
    else:
        form = RoomForm()
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
    return render(request, "chat/roomchat.html", {"pending_rooms": pending_rooms, "joined_rooms": joined_rooms, "form": form})

@login_required
def invite_rooms(request):
    if request.method == 'POST':
        form = RoomRegistrationForm(request.POST)
        
        if form.is_valid():
            room_reg  = form.save(commit=False)
            room_reg.status = 'PENDING'
            room_reg.save()
            return redirect('invite-rooms')
    else:
        form = RoomRegistrationForm()
    # we will get the chatbox name from the url
    rooms_registration = RoomRegistration.objects.filter(user=request.user, status='JOINED')

    joined_rooms = []
    for r in rooms_registration:
       joined_rooms.append(r.room)
       
    return render(request, "chat/inviteroom.html", {"joined_rooms": joined_rooms, "form": form})

@login_required
def pending_rooms(request, slug, option):
    ##delete or update the pending options
    rooms = Room.objects.filter(slug=slug)
    if len(rooms)==1:
        room = rooms[0]
        room_registrations = RoomRegistration.objects.filter(user=request.user, room=room)
        room_registration = room_registrations.first()
        if room_registration:
            if option=='accepted':
                room_registration.status = 'JOINED'
                room_registration.save()
            else:
                room_registration.delete();
        
    return redirect('rooms')