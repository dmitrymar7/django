from django.contrib import admin
from .models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # fields = ['title', 'cooking_time', 'author', 'image', 'time_create']
    list_display = ['title', 'cooking_time', 'author', 'image', 'time_create']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

