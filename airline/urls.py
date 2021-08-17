from django.urls import path
from .import views

urlpatterns = [
    path('', views.airline, name='airline-home'),
    path('search_flight', views.search_flight, name='airline-search'),
    path('search_output', views.search_output, name='search-output'),
]
