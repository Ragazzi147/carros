# Generated by Django 4.2.1 on 2023-06-03 08:47

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.upload_image_car),
        ),
    ]