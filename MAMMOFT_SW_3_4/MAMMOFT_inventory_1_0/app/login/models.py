from django.db import models
import datetime
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import string
import random

def calculate_hash(size=20, chars=string.ascii_uppercase + string.digits):
    return str(''.join(random.choice(chars) for _ in range(size)))

class U_hash(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hash = models.CharField(max_length=20, default=calculate_hash)
    avatar = models.ImageField(max_length=300, upload_to = "login/users/profile", default="/media/login/users/profile/none/default_avatar.png")
    f_nacimiento = models.DateTimeField(auto_now_add=True, blank=True)
    edad = models.CharField(max_length=3, default="0")
    sexo = models.CharField(max_length=15, default="No definido")
    cargo = models.CharField(max_length=100, default="Sin cargo")
    direccion = models.CharField(max_length=200, default="Sin dirección")

    #Método que crea el hash
    def add_hash(sender, instance, created, **kwargs):
        if created:
            U_hash.objects.create(user=instance)
    post_save.connect(add_hash, sender=User, dispatch_uid="add_hash")
