# Generated by Django 4.2.1 on 2023-06-03 08:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id_car', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('km', models.CharField(max_length=100)),
                ('cambio', models.CharField(max_length=100)),
            ],
        ),
    ]
