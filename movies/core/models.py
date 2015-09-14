from django.db import models
from django.template.defaultfilters import slugify

class Movie (models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField('Category', blank=True, null=True)
    author = models.ManyToManyField('Author', blank=True, null=True)
    description = models.TextField()
    # slug = models.SlugField(blank=True, editable=False, null=True)
    slug = models.SlugField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

class Category (models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True)
    create_time = models.DateTimeField(null=True,auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Author (models.Model):
    name = models.CharField(max_length=200, unique=True)
    nationality = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    create_time = models.DateTimeField(null=True,auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)