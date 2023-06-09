from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

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


def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)
