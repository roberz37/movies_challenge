from celery import shared_task
import requests
import pandas as pd
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MovieRating

@shared_task
def analyze_movies_scores():
    api_key = settings.MOVIE_DB_API_KEY # Utiliza el movie api key default
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&page='

    data = []
    for page in range(1, 11):
        response = requests.get(url + str(page))
        movies = response.json().get('results', [])
        for movie in movies:
            release_date = movie.get('release_date', '')[:4]
            vote_average = movie.get('vote_average', 0)
            data.append({'year': release_date, 'score': vote_average})

    df = pd.DataFrame(data)
    result = df.groupby('year')['score'].agg(['mean', 'count']).reset_index()
    result.columns = ['year', 'vote_average', 'quantity']
    result = result.to_dict('records')
    for movie in result:
        MovieRating.objects.create(year=int(movie['year']),
                                   vote_average=float(movie['vote_average']),
                                   quantity=int(movie['quantity']))

    return HttpResponse(result, status = 200)
