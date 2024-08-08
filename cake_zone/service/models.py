from django.db import models


class Services_Cafe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()