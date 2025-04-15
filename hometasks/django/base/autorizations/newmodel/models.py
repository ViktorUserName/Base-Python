from django.db import models

class NewModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
