from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    ingredients = models.TextField(blank=True, verbose_name='Ингредиенты')
    cooking_steps = models.TextField(blank=True, verbose_name='Шаги приготовления')
    cooking_time = models.IntegerField(blank=True, default=0, verbose_name='Время приготовления (минут)')
    image = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        default=None,
        null=True,
        verbose_name='Изображение'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='recipes',
        null=True,
        default=None,
        verbose_name='Автор'
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    category = models.ManyToManyField(
        'Category',
        blank=True,
        related_name='category_recipies',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

