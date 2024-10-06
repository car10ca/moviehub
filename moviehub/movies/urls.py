from django.urls import path, include
from .views import (
    frontend_home_view, movie_list, movie_detail, 
    movie_create, movie_update, movie_delete, actors_with_director_view, 
    top_grossing_movies_view, actors_list, directors_list, top_directors,
    top_versatile_directors, top_directors_by_imdb_view, top_movies_by_imdb,
    movies_by_year_genre, movies_by_actor, movies_by_content_rating, movies_by_language
)

urlpatterns = [
    path('', frontend_home_view, name='frontend_home'),  #frontend home view
    path('movies/', movie_list, name='movie_list'),  #list all movies
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),  #movie detail view
    path('movies/new/', movie_create, name='movie_create'),  #create a new movie
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),  #edit a movie
    path('movies/<int:pk>/delete/', movie_delete, name='movie_delete'),  #delete a movie
    path('actors_with_director/', actors_with_director_view, name='actors_with_director'),  #view actors with a director
    path('movies/top_grossing/', top_grossing_movies_view, name='top_grossing_movies'),  #top grossing movies
    path('directors/', directors_list, name='directors_list'),  #list all directors
    path('top_directors/', top_directors, name='top_directors'),  #top directors by gross earnings
    path('actors/', actors_list, name='actors_list'),  #list all actors
    path('top_versatile_directors/', top_versatile_directors, name='top_versatile_directors'),  #top versatile directors
    path('top_directors_by_imdb/', top_directors_by_imdb_view, name='top_directors_by_imdb'),  #top directors by IMDb score
    path('top_movies_by_imdb/', top_movies_by_imdb, name='top_movies_by_imdb'),  #top movies by IMDb score
    path('movies_by_year_genre/', movies_by_year_genre, name='movies_by_year_genre'), #filter movies by year & genre
    path('movies_by_actor/', movies_by_actor, name='movies_by_actor'), #select actor and see all movies they're in
    path('movies_by_content_rating/', movies_by_content_rating, name='movies_by_content_rating'), #filter movies by content rating
    path('movies_by_language/', movies_by_language, name='movies_by_language'), #filter movies by language
    path('api/', include('movies.api_urls', namespace='api')),  #include API URLs with namespace
]
