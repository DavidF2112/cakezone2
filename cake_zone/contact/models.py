from django.db import models

class Information_Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    
