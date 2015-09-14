from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from movies.core.views import MovieListView, MovieDetailView, AuthorDetailView

urlpatterns = patterns('movies.core.views',
    url(r'^filme/(?P<slug>[-_\w]+)/$', MovieDetailView.as_view(), name='movie-detail'),
    url(r'^autor/(?P<slug>[-_\w]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^filme$', MovieListView.as_view(), name='movie-list'),
    url(r'^$', 'homepage', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
