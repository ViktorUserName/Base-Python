from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
