# Generated by Django 4.0 on 2022-12-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_chat', '0007_alter_message_options_alter_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(blank='False', max_length=20, unique=True),
        ),
    ]
