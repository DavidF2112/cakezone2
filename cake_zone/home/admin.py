from django.contrib import admin
from .models import Information_Cafe, Review_Clients
from django.utils.safestring import mark_safe
# Register your models here.


admin.site.register(Information_Cafe)



@admin.register(Review_Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('photo_tag','name','description','is_visible','sort','grade',)
    list_filter = ('is_visible',)
    search_fields = ('name',)
    list_editable = ('is_visible',)


    def photo_tag(self , obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" width = "50" height ="50" />')
    photo_tag.short_description = 'Photo'