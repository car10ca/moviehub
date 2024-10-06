from django.urls import path
from .api_views import (
    MovieListView, MovieDetailView, DirectorListView, ActorListView, GenreMovieListView,
    top_10_highest_grossing_movies, actors_with_director, list_directors, top_directors_by_imdb,
    top_versatile_directors, api_home_view
)

app_name = 'api'

urlpatterns = [
    path('', api_home_view, name='api_home'),  # API home endpoint
    path('movies/', MovieListView.as_view(), name='movie_list'),  # List and create movies
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),  # Retrieve, update, and delete a movie
    path('directors/', DirectorListView.as_view(), name='director_list'),  # List all directors
    path('directors/all/', list_directors, name='list_directors'),  # List all directors for dropdown
    path('actors/', ActorListView.as_view(), name='actor_list'),  # List all actors
    path('movies_by_genre/<str:genre>/', GenreMovieListView.as_view(), name='movies_by_genre'),  # List movies by genre
    path('movies/top_grossing/', top_10_highest_grossing_movies, name='top_10_highest_grossing_movies'),  # Top 10 highest grossing movies
    path('directors/<int:director_id>/actors/', actors_with_director, name='actors_with_director'),  # Actors who worked with a given director
    path('directors/top_by_imdb/', top_directors_by_imdb, name='top_directors_by_imdb'),  # Top directors by IMDb score
    path('directors/top_versatile/', top_versatile_directors, name='top_versatile_directors'),  # Top versatile directors
]
