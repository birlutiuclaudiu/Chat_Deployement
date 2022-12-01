from django.urls import path
from  django.contrib.auth import views as authentication_views


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', authentication_views.LogoutView.as_view(), name='logout'),
    path("login/", authentication_views.LoginView.as_view(template_name="chat/login.html"), name="login"),
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    
]