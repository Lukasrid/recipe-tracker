from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Cuisine(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Recipe(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    dish = models.CharField(max_length=200)
    cuisine = models.ForeignKey(Cuisine, null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.dish


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]