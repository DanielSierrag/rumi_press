# Generated by Django 5.2 on 2025-04-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
