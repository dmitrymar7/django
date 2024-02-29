from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag()
def get_menu():
    menu = [
        {'name': 'Главная', 'url': reverse_lazy('main'), 'service_name': 'main'},
        {'name': 'Мои рецепты', 'url': reverse_lazy('my_recipes'), 'service_name': 'my_recipes'},
        {'name': 'Добавить рецепт', 'url': reverse_lazy('add_recipe'), 'service_name': 'add_recipe'}
    ]

    return menu


@register.inclusion_tag('Recipe/menu.html')
def show_menu(service_menu_name=None):
    menu = get_menu()
    return {'menu': menu, 'service_menu_name': service_menu_name}
