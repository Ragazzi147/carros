from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models he((re.


class CustomUser(AbstractUser):
    # Adicione campos personalizados aqui
    # Exemplo: idade = models.IntegerField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)

    # Adicione mais campos personalizados conforme necessário

    def __str__(self):
        return self.username


def upload_image_car(instance, filename):
    return f"{instance.id_car}-{filename}"


class app(models.Model):
    id_car = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    km = models.CharField(max_length=100)
    cambio = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_car, blank=True, null=True)
