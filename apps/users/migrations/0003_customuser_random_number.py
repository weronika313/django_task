# Generated by Django 3.2.4 on 2021-06-27 14:35

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='random_number',
            field=models.IntegerField(default=apps.users.models.random_number),
        ),
    ]