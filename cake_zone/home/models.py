from django.db import models

class Information_Cafe(models.Model):
    name = models.CharField(max_length=50)
    year_create = models.IntegerField()
    is_open = models.BooleanField(default=True)
    description = models.TextField()


class Review_Clients(models.Model):
    name_client = models.CharField(max_length=50)
    grade = models.IntegerField()
    sort = models.PositiveSmallIntegerField()
    description = models.TextField()