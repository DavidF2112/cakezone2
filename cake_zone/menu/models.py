from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        return iter(self.dishes.filter(is_visible=True))

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('sort' , )



class Dish(models.Model):
    name = models.CharField(max_length=50)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='menu_photos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Dish'
        ordering = ('sort' , )