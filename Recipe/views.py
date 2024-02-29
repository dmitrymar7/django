from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from . import models, forms


def main(request):

    data = {
        'recipes': models.Recipe.objects.all(),
        'categories':
            models.Category.objects.annotate(
                count_recipes=models.models.Count('category_recipies')).filter(count_recipes__gt=0),
        'category_id': 0,
        'service_menu_name': 'main',
        'url_category': 'category'
    }
    return render(request, 'Recipe/main.html', context=data)


@login_required
def my_recipes(request):
    queryset_categories = models.Category.objects.annotate(
        count_recipes=models.models.Count('category_recipies')).filter(count_recipes__gt=0, category_recipies__author=request.user)

    data = {
        'recipes': models.Recipe.objects.filter(author=request.user),
        'categories': queryset_categories,
        'category_id': 0,
        'service_menu_name': 'my_recipes',
        'url_category': 'my_recipe_category'
    }
    return render(request, 'Recipe/main.html', context=data)


def my_recipe_category(request, category_id=0):
    if category_id < 1:
        return redirect('my_recipes')

    category = get_object_or_404(models.Category, pk=category_id)

    queryset_categories = models.Category.objects.annotate(
        count_recipes=models.models.Count('category_recipies')).filter(count_recipes__gt=0,
                                                                       category_recipies__author=request.user)

    data = {
        'recipes': models.Recipe.objects.filter(category__id=category.pk, author=request.user),
        'categories': queryset_categories,
        'category_id': category_id,
        'service_menu_name': 'my_recipes',
        'url_category': 'my_recipe_category'
    }

    return render(request, 'Recipe/main.html', context=data)


def recipe_category(request, category_id=0):
    if category_id < 1:
        return redirect('main')

    category = get_object_or_404(models.Category, pk=category_id)

    data = {
        'recipes': models.Recipe.objects.filter(category__id=category.pk),
        'categories': models.Category.objects.annotate(
            count_recipes=models.models.Count('category_recipies')
        ).filter(count_recipes__gt=0),
        'category_id': category_id,
        'service_menu_name': 'main',
        'url_category': 'category'
    }

    return render(request, 'Recipe/main.html', context=data)


def recipe(request, recipe_id):

    obj_recipe = get_object_or_404(models.Recipe, pk=recipe_id)

    data = {
        'recipe': obj_recipe
    }
    return render(request, 'Recipe/recipe.html', context=data)


class AddRecipe(LoginRequiredMixin, CreateView):
    form_class = forms.AddPostForm
    model = models.Recipe
    template_name = 'Recipe/add_recipe.html'
    context_object_name = 'recipe'

    def get_success_url(self):
       recipe = self.object
       if recipe is not None:
           return reverse('recipe', args=[recipe.id])

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.cooking_time = recipe.cooking_time if recipe.cooking_time is not None else 0
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление рецепта'
        return context


class UpdateRecipe(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    fields = '__all__'
    template_name = 'Recipe/add_recipe.html'
    context_object_name = 'recipe'

    def get_success_url(self):
        recipe = self.object
        if recipe is not None:
            return reverse('recipe', args=[recipe.id])


class DetailRecipe(UpdateView):
    model = models.Recipe
    fields = '__all__'
    template_name = 'Recipe/recipe.html'
    success_url = reverse_lazy('main')
    context_object_name = 'recipe'


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    recipe.delete()

    return redirect('main')

