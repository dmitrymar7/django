from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<int:category_id>', views.recipe_category, name='category'),
    path('recipe/<int:pk>', views.DetailRecipe.as_view(), name='recipe'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('edit_recipe/<int:pk>', views.UpdateRecipe.as_view(), name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('my_recipe_category/<int:category_id>', views.my_recipe_category, name='my_recipe_category')
]
