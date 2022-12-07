#pip install django-online-users
#https://pypi.org/project/django-online-users/

from datetime import timedelta
from online_users.models import OnlineUserActivity
from django.core.mail import send_mail
from django.conf import settings

def is_online(user):
    user_activity_objects = OnlineUserActivity.get_user_activities(timedelta(minutes=1))
    activities = (user for user in user_activity_objects)
    return user in [activity.user for activity in activities]

def sendEmail(email, message):
    subject = 'A new message'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
