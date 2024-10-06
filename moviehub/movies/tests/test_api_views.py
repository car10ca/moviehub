# movies/test_api_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from movies.models import Movie
from movies.factories import MovieFactory, DirectorFactory, ActorFactory, GenreFactory, LanguageFactory, CountryFactory, ContentRatingFactory

class MovieAPITests(APITestCase):
    def setUp(self):
        # Create test data using factories
        self.director = DirectorFactory()
        self.language = LanguageFactory()
        self.country = CountryFactory()
        self.content_rating = ContentRatingFactory()
        self.actor = ActorFactory()
        self.genre = GenreFactory()
        self.movie = MovieFactory(
            director=self.director,
            language=self.language,
            country=self.country,
            content_rating=self.content_rating,
            duration=120  # Ensure duration is provided
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)
    
    def test_create_movie_api(self):
        # Data for creating a new movie
        data = {
            'title': 'New Movie',
            'director': self.director.id,
            'duration': 120,  # Ensure duration is provided
            'gross': 2000000,
            'language': self.language.id,
            'country': self.country.id,
            'content_rating': self.content_rating.id,
            'budget': 1000000,
            'year': 2022,
            'imdb_score': 9.0,
            'actors': [self.actor.id],
            'genres': [self.genre.id]
        }
        response = self.client.post(reverse('api:movie_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Movie.objects.filter(title='New Movie').exists())

    def test_update_movie_api(self):
        # Data for updating an existing movie
        data = {
            'title': 'Updated Movie',
            'director': self.director.id,
            'duration': 130,  # Ensure duration is provided
            'gross': 1500000,
            'language': self.language.id,
            'country': self.country.id,
            'content_rating': self.content_rating.id,
            'budget': 750000,
            'year': 2023,
            'imdb_score': 8.0,
            'actors': [self.actor.id],
            'genres': [self.genre.id]
        }
        response = self.client.put(reverse('api:movie_detail', args=[self.movie.id]), data, format='json')
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Updated Movie')
