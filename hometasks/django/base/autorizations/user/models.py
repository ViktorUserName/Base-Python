from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('author', 'Автор'),
        ('reader', 'Читатель'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='author')

    def __str__(self):
        return f'{self.username} -- ({self.role})'

class Token(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=120, unique=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)