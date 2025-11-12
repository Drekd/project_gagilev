from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import main, index2

urlpatterns = [
    path('', main, name=''),
    path('Car', index2, name='car')
]