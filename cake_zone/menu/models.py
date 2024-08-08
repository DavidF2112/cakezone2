from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='menu_photos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)