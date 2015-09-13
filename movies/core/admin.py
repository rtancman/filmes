from django.contrib import admin
from .models import Movie, Author, Category

# Register your models here.
admin.site.register(Movie)
admin.site.register(Author)
admin.site.register(Category)