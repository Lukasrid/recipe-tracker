from django.contrib import admin
from .models import Images


from .models import Cuisine, Recipe, Comment, Images

admin.site.register(Cuisine)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Images)
