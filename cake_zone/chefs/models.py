from django.db import models

class Chefs_Information(models.Model):
    name = models.CharField(max_length=50,default=None)
    position = models.CharField(max_length=50,default=None)
    photo = models.ImageField(upload_to='staff_photos',default=None)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(default=0)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ('sort', )

    def __str__(self):
        return self.name