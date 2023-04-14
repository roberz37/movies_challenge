from django.urls import path
from . import views

urlpatterns = [
    path('collect_data/', views.collect_data, name='collect_data'),
    path('movies_list/', views.movies_list, name='movies_list'),
]