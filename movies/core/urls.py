from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('movies.core.views',
    # Examples:
    url(r'^$', 'homepage', name='homepage'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
