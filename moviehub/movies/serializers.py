from rest_framework import serializers
from .models import Movie, Director, Actor, Genre, Language, Country, ContentRating


#================================== FrontEnd ==================================
#detailed serializers for frontend and nested relationships
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ContentRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentRating
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    language = LanguageSerializer()
    country = CountrySerializer()
    content_rating = ContentRatingSerializer()
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    duration = serializers.IntegerField()  

    class Meta:
        model = Movie
        fields = '__all__'

class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title', 'director', 'duration', 'gross', 'language', 
            'country', 'content_rating', 'budget', 'year', 'imdb_score', 
            'actors', 'genres'
        ]

#================================== API ==================================
#simplified serializers for API usage
class SimpleDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class SimpleActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']

class SimpleGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class SimpleLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class SimpleCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class SimpleContentRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentRating
        fields = ['id', 'rating']

class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_score', 'gross', 'director', 'language', 'country', 'content_rating', 'actors', 'genres']
