from django.contrib import admin


from .models import Cuisine, Recipe, Comment

admin.site.register(Cuisine)
admin.site.register(Recipe)
admin.site.register(Comment)

