# Generated by Django 4.0 on 2022-12-02 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aso_chat', '0002_room_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='joined_users',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
