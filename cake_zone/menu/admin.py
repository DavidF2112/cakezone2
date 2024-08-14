from django.contrib import admin
from .models import Category,Dish
from django.utils.safestring import mark_safe
# Register your models here.



class DishInline(admin.TabularInline):
    model = Dish
    fields = ('name', 'price', 'is_visible', 'sort')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (DishInline, )
    list_display = ('name', 'is_visible', 'sort')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id','photo_tag' , 'name' , 'is_visible','sort',)
    list_filter = ('is_visible',)
    search_fields = ('name',)
    list_editable = ('name' , 'is_visible')

    def photo_tag(self , obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width = "50" height ="50" />')
    photo_tag.short_description = 'Photo'