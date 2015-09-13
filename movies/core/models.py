from django.db import models

class Movie (models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField('Category')
    author = models.ManyToManyField('Author')
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

class Category (models.Model):
    name = models.CharField(max_length=100, unique=True)

class Author (models.Model):
    name = models.CharField(max_length=200, unique=True)
    nationality = models.CharField(max_length=100)