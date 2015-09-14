from django.contrib import admin
from movies.core.models import Movie, Author, Category

# class MovieInline(admin.TabularInline):
#     model = Movie
#     extra = 10

# class AuthorInline(admin.TabularInline):
#     model = Author
#     extra = 10

class MovieAdmin(admin.ModelAdmin):
    # inlines = (AuthorInline,)
    list_display  = ('name', 'description', 'slug', 'create_time', )
    prepopulated_fields = {'slug': ('name',)}

class AuthorAdmin(admin.ModelAdmin):
    # inlines = (MovieInline,)
    list_display  = ('name', 'nationality', )

class CategoryAdmin(admin.ModelAdmin):
    # inlines = (MovieInline,)
    list_display  = ('name', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)