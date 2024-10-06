import factory
from faker import Faker
from .models import Movie, Director, Actor, Genre, Language, Country, ContentRating

fake = Faker()

class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Director
    
    name = factory.Faker('name')

class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor
    
    name = factory.Faker('name')

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre
    
    name = factory.Faker('word')

class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language
    
    name = factory.Faker('language_name')

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    
    name = factory.Faker('country')

class ContentRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentRating
    
    rating = factory.Faker('random_element', elements=['G', 'PG', 'PG-13', 'R', 'NC-17'])

class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie
    
    title = factory.Faker('sentence', nb_words=3)
    director = factory.SubFactory(DirectorFactory)
    duration = factory.Faker('random_int', min=60, max=240)  # Assuming duration is in minutes
    gross = factory.Faker('random_int', min=100000, max=10000000)
    language = factory.SubFactory(LanguageFactory)
    country = factory.SubFactory(CountryFactory)
    content_rating = factory.SubFactory(ContentRatingFactory)
    budget = factory.Faker('random_int', min=100000, max=5000000)
    year = factory.Faker('year')
    imdb_score = factory.Faker('pyfloat', positive=True, min_value=1.0, max_value=10.0)
