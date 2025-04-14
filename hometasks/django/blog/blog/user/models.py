from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'Admin', 'admin'
        AUTHOR = 'Author', 'author'
        READER = 'Reader', 'reader'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)
