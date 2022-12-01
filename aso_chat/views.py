from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

from .forms.forms import RegisterForm
# Create your views here.
def index(request):
    return render(request, "chat/base.html", {})

def home(request):
     return render(request, "chat/home.html", {})

def register(request):
 
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        newUser = registerForm.save()
        login(request, newUser)
        return redirect('home')
    
    else:
        print("NUUUUU")
        registerForm = RegisterForm()
    dictionary = {}
    dictionary['form'] = registerForm
    return render(request, "chat/register.html", dictionary)

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name})