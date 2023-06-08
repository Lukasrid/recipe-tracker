from django.shortcuts import render
from .models import Recipe

# recipes = [
#     {'id': 1, 'name': 'Savoury'},
#     {'id': 2, 'name': 'Sweet'},
# ]


def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'base/home.html', {'recipes': recipes})


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html', context)
