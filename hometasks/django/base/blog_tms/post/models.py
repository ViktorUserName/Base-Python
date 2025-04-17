from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title