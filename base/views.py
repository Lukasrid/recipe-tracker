from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Cuisine
from .forms import RecipeForm

# recipes = [
#     {'id': 1, 'name': 'Savoury'},
#     {'id': 2, 'name': 'Sweet'},
# ]


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password is incorrect')

    context = {}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    recipes = Recipe.objects.filter(
        Q(cuisine__type__icontains=q) | 
        Q(dish__icontains=q) | 
        Q(description__icontains=q) |
        Q(ingredients__icontains=q)
        )

    cuisines = Cuisine.objects.all()
    recipes_count = recipes.count()

    context = {'recipes': recipes, 'cuisines': cuisines, 'recipes_count': recipes_count}
    return render(request, 'base/home.html', context)


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


def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':recipe})