# Generated by Django 4.2.2 on 2023-06-16 11:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_picture_remove_recipe_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
