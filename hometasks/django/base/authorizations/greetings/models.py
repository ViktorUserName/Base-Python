from django.db import models

class Greetings(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
