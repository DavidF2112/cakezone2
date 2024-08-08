from django.db import models

class Chefs_Information(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField()