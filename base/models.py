from django.db import models


class Recipe(models.Model):
    dish = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dish
