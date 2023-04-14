from django.http import HttpResponse, JsonResponse
from . import tasks
from .models import MovieRating
from django.shortcuts import render

# Create your views here.
    
def collect_data(request):
    result = tasks.analyze_movies_scores()
    return HttpResponse(result)

def movies_list(request):
    movies = MovieRating.objects.all()
    return render(request, 'base.html', {'movies': movies})