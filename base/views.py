from django.shortcuts import render

recipes = [
    {'id': 1, 'name': 'Savoury'},
    {'id': 2, 'name': 'Sweet'},
]


def home(request):
    context = {'recipes': recipes}
    return render(request, 'base/home.html', {'recipes': recipes})


def recipe(request, pk):
    recipe = None
    for i in recipes:
        if i['id'] == int(pk):
            recipe = i
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html', context)
