from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass



class Newsletters(models.Model):
    email= models.EmailField()


    def __str__(self) -> str:
        return self.email