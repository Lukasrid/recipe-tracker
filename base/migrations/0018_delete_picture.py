# Generated by Django 4.2.2 on 2023-06-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_picture_remove_recipe_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
