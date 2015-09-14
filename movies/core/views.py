from movies.core.models import Movie, Author, Category
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

class MovieListView(ListView):

    model = Movie
    context_object_name = "movies"

    def get_queryset(self):
        order = self.request.GET.get("order", "asc")
        if order == "desc":
            return Movie.objects.all().order_by("-id")
        else:
            return Movie.objects.all()

class MovieDetailView(DetailView):

    model = Movie

    def get_context_data(self, **kwargs):
        return super(MovieDetailView, self).get_context_data(**kwargs)

class AuthorDetailView(DetailView):

    model = Author

    def get_context_data(self, **kwargs):
        return super(AuthorDetailView, self).get_context_data(**kwargs)