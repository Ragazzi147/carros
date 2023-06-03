from django.db import models
from uuid import uuid4

# Create your models he((re.
def upload_image_car(instance, filename):
    return f"{instance.id_car}-{filename}"

class app(models.Model):
    id_car = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    km = models.CharField(max_length=100)
    Cambio = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_car, blank=True, null=True)