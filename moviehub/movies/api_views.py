from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import Count, Avg
from django.http import JsonResponse
from .models import Movie, Director, Actor, Genre, MovieActor
from .serializers import (
    MovieSerializer, SimpleMovieSerializer,
    DirectorSerializer, SimpleDirectorSerializer,
    ActorSerializer, SimpleActorSerializer,
    GenreSerializer, MovieCreateUpdateSerializer
)

#================== CLASS BASED VIEWS ==================
class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    permission_classes = [AllowAny]

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    permission_classes = [AllowAny]

class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = SimpleDirectorSerializer  # use the simplified serializer
    permission_classes = [AllowAny]

class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = SimpleActorSerializer  # use the simplified serializer
    permission_classes = [AllowAny]

class GenreMovieListView(generics.ListAPIView):
    serializer_class = SimpleMovieSerializer  # use the simplified serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        genre_name = self.kwargs['genre']
        return Movie.objects.filter(genres__name=genre_name)



#================== FUNCTION BASED VIEWS ==================
@api_view(['GET'])
def api_home_view(request):
    # provide a description of the available API endpoints
    api_description = {
        "description": "Welcome to the Moviehub API. This API provides access to movie-related data, including movies, directors, actors, and more.",
        "endpoints": {
            "movies": {
                "url": "/api/movies/",
                "method": "GET",
                "description": "Retrieve a list of all movies."
            },
            "movie_detail": {
                "url": "/api/movies/{id}/",
                "method": "GET",
                "description": "Retrieve the details of a specific movie by its ID."
            },
            "create_movie": {
                "url": "/api/movies/",
                "method": "POST",
                "description": "Create a new movie."
            },
            "update_movie": {
                "url": "/api/movies/{id}/",
                "method": "PUT",
                "description": "Update an existing movie by its ID."
            },
            "delete_movie": {
                "url": "/api/movies/{id}/",
                "method": "DELETE",
                "description": "Delete an existing movie by its ID."
            },
            "top_grossing_movies": {
                "url": "/api/movies/top-grossing/",
                "method": "GET",
                "description": "Retrieve the top 10 highest grossing movies."
            },
            "directors": {
                "url": "/api/directors/",
                "method": "GET",
                "description": "Retrieve a list of all directors."
            },
            "director_detail": {
                "url": "/api/directors/{id}/",
                "method": "GET",
                "description": "Retrieve the details of a specific director by their ID."
            },
            "actors": {
                "url": "/api/actors/",
                "method": "GET",
                "description": "Retrieve a list of all actors."
            },
            "actor_detail": {
                "url": "/api/actors/{id}/",
                "method": "GET",
                "description": "Retrieve the details of a specific actor by their ID."
            },
            "movies_by_genre": {
                "url": "/api/movies_by_genre/{genre}/",
                "method": "GET",
                "description": "Retrieve a list of movies filtered by genre."
            },
            "actors_with_director": {
                "url": "/api/directors/{director_id}/actors/",
                "method": "GET",
                "description": "Select a director to see which actors they've worked with and how often."
            },
            "top_directors_by_imdb": {
                "url": "/api/directors/top-by-imdb/",
                "method": "GET",
                "description": "Retrieve the top directors based on average IMDb scores."
            },
            "top_versatile_directors": {
                "url": "/api/directors/top-versatile/",
                "method": "GET",
                "description": "Retrieve the top versatile directors who have worked with the most unique actors."
            },
            "list_directors": {
                "url": "/api/directors/all/",
                "method": "GET",
                "description": "Retrieve a list of all directors for selection in actors_with_director."
            }
        }
    }
    return JsonResponse(api_description)



@api_view(['GET'])
def actors_with_director(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    actor_counts = MovieActor.objects.filter(movie__director=director).values('actor__name').annotate(count=Count('actor')).order_by('-count')
    actors = [{'name': actor['actor__name'], 'count': actor['count']} for actor in actor_counts]
    return Response(actors)

@api_view(['GET'])
def top_10_highest_grossing_movies(request):
    movies = Movie.objects.order_by('-gross')[:10]
    serializer = SimpleMovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_directors(request):
    directors = Director.objects.all()
    serializer = SimpleDirectorSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def top_directors_by_imdb(request):
    directors = Director.objects.annotate(average_imdb=Avg('movie__imdb_score')).order_by('-average_imdb')[:10]
    data = [{'name': director.name, 'average_imdb': director.average_imdb} for director in directors]
    return Response(data)

@api_view(['GET'])
def top_versatile_directors(request):
    directors = Director.objects.annotate(unique_actors=Count('movie__movieactor__actor', distinct=True)).order_by('-unique_actors')[:5]
    data = [{'name': director.name, 'unique_actors': director.unique_actors} for director in directors]
    return Response(data)
