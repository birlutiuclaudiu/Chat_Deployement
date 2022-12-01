from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

from .forms.forms import RegisterForm

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
        print("NUUUUU")
        registerForm = RegisterForm()
    
    return render(request, "chat/register.html", {'form':registerForm })

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name})