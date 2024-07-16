from django.urls import path
from .views import search

urlpatterns = [
    path('search/', search.as_view(), name='searchcourse'),
]
