from django.db import models

class Information_Cafe(models.Model):
    name = models.CharField(max_length=50)
    year_create = models.IntegerField()
    is_open = models.BooleanField(default=True)
    description = models.TextField()


class Review_Clients(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    photo = models.ImageField(upload_to="home_photos" ,blank=True , null=True)
    sort = models.PositiveSmallIntegerField()
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name_plural = 'Client'
        ordering = ('sort' , )

    def __str__(self):
        return self.name