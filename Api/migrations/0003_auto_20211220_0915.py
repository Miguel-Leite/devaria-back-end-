# Generated by Django 3.2.3 on 2021-12-20 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_rename_phone_no_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
