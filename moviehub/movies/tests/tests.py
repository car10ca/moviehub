from django.test import TestCase, Client
from django.urls import reverse
from movies.models import Movie, Director, Actor, Genre, Language, Country, ContentRating
from movies.forms import MovieForm
from movies.factories import MovieFactory, DirectorFactory, ActorFactory, GenreFactory, LanguageFactory, CountryFactory, ContentRatingFactory

#===================== MOVIE TESTS =====================

class MovieTests(TestCase):
    def setUp(self):
        #create test data using factory boy
        self.director = DirectorFactory(name="Test Director")
        self.language = LanguageFactory(name="English")
        self.country = CountryFactory(name="USA")
        self.content_rating = ContentRatingFactory(rating="PG-13")
        self.genre = GenreFactory(name="Action")
        self.actor = ActorFactory(name="Test Actor")
        
        self.movie = MovieFactory(
            title="Test Movie",
            director=self.director,
            duration=120,
            gross=1000000,
            language=self.language,
            country=self.country,
            content_rating=self.content_rating,
            budget=500000,
            year=2023,
            imdb_score=8.5
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)
    
    def test_movie_list_view(self):
        #test the movie list view
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movie_list.html')
        self.assertContains(response, self.movie.title)

    def test_movie_detail_view(self):
        #test the movie detail view
        response = self.client.get(reverse('movie_detail', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movie_detail.html')
        self.assertContains(response, self.movie.title)

    def test_movie_create_view(self):
        #test the movie create view
        response = self.client.post(reverse('movie_create'), {
            'title': 'New Movie',
            'director': self.director.id,
            'duration': 150,
            'gross': 2000000,
            'language': self.language.id,
            'country': self.country.id,
            'content_rating': self.content_rating.id,
            'budget': 1000000,
            'year': 2022,
            'imdb_score': 9.0,
            'actors': [self.actor.id],
            'genres': [self.genre.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Movie.objects.filter(title='New Movie').exists())

    def test_movie_update_view(self):
        #test the movie update view
        response = self.client.post(reverse('movie_update', args=[self.movie.id]), {
            'title': 'Updated Movie',
            'director': self.director.id,
            'duration': 130,
            'gross': 1500000,
            'language': self.language.id,
            'country': self.country.id,
            'content_rating': self.content_rating.id,
            'budget': 750000,
            'year': 2023,
            'imdb_score': 8.0,
            'actors': [self.actor.id],
            'genres': [self.genre.id]
        })
        self.assertEqual(response.status_code, 302)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Updated Movie')

    def test_movie_delete_view(self):
        #test the movie delete view
        response = self.client.post(reverse('movie_delete', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())


#===================== DIRECTOR TESTS =====================

class DirectorTests(TestCase):
    def setUp(self):
        #create test data for director tests using factory boy
        self.director = DirectorFactory(name="Test Director")
        MovieFactory(
            title="Test Movie",
            director=self.director,
            duration=120,
            gross=1000000,
            language=LanguageFactory(name="English"),
            country=CountryFactory(name="USA"),
            content_rating=ContentRatingFactory(rating="PG-13"),
            budget=500000,
            year=2023,
            imdb_score=8.5
        )
    
    def test_directors_list_view(self):
        #test the directors list view
        response = self.client.get(reverse('directors_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/directors_list.html')
        self.assertContains(response, self.director.name)

    def test_top_directors_view(self):
        #test the top directors view
        response = self.client.get(reverse('top_directors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/top_directors.html')

    def test_top_versatile_directors_view(self):
        #test the top versatile directors view
        response = self.client.get(reverse('top_versatile_directors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/top_versatile_directors.html')

    def test_top_directors_by_imdb_view(self):
        #test the top directors by IMDb view
        response = self.client.get(reverse('top_directors_by_imdb'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/top_directors_by_imdb.html')
        self.assertContains(response, self.director.name)
        self.assertContains(response, "8.5")


#===================== ACTOR TESTS =====================

class ActorTests(TestCase):
    def setUp(self):
        #create test data for actor tests using factory boy
        self.actor = ActorFactory(name="Test Actor")
    
    def test_actors_list_view(self):
        #test the actors list view
        response = self.client.get(reverse('actors_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/actors_list.html')
        self.assertContains(response, self.actor.name)

    def test_actors_with_director_view(self):
        #test the actors with director view
        response = self.client.get(reverse('actors_with_director'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/actors_with_director.html')

    def test_movies_by_actor_view(self):
        #test the movies by actor view
        response = self.client.get(reverse('movies_by_actor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movies_by_actor.html')


#===================== FILTER TESTS =====================

class FilterTests(TestCase):
    def setUp(self):
        #create test data for filter tests using factory boy
        self.director = DirectorFactory(name="Test Director")
        self.language = LanguageFactory(name="English")
        self.country = CountryFactory(name="USA")
        self.content_rating = ContentRatingFactory(rating="PG-13")
        self.genre = GenreFactory(name="Action")
        self.actor = ActorFactory(name="Test Actor")
        
        self.movie = MovieFactory(
            title="Test Movie",
            director=self.director,
            duration=120,
            gross=1000000,
            language=self.language,
            country=self.country,
            content_rating=self.content_rating,
            budget=500000,
            year=2023,
            imdb_score=8.5
        )
        self.movie.actors.add(self.actor)
        self.movie.genres.add(self.genre)

    def test_movies_by_year_genre_view(self):
        #test the movies by year and genre view
        response = self.client.get(reverse('movies_by_year_genre'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movies_by_year_genre.html')

    def test_movies_by_content_rating_view(self):
        #test the movies by content rating view
        response = self.client.get(reverse('movies_by_content_rating'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movies_by_content_rating.html')

    def test_movies_by_language_view(self):
        #test the movies by language view
        response = self.client.get(reverse('movies_by_language'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movies_by_language.html')
