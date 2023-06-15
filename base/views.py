from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Cuisine, Comment
from .forms import RecipeForm

# recipes = [
#     {'id': 1, 'name': 'Savoury'},
#     {'id': 2, 'name': 'Sweet'},
# ]


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


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
    recipe_comments = Comment.objects.filter(Q(recipe__cuisine__type__icontains=q))

    context = {'recipes': recipes, 'cuisines': cuisines, 'recipes_count': recipes_count, 'recipe_comments': recipe_comments}
    return render(request, 'base/home.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe_comments = recipe.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            recipe=recipe,
            body=request.POST.get('body')
        )
        return redirect('recipe', pk=recipe.id)

    context = {'recipe': recipe, 'recipe_comments': recipe_comments}
    return render(request, 'base/recipe.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


@login_required(login_url='login')
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.user != recipe.user:
        return HttpResponse('This is not your recipe to edit!!')

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


@login_required(login_url='login')
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.user != recipe.user:
        return HttpResponse('This is not your recipe to delete!!')

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':recipe})


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('This is not your comment to delete!!')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':comment})