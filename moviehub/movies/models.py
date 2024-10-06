from django.db import models

class Director(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    name = models.CharField(max_length=255, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.name
    

class Actor(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    name = models.CharField(max_length=255, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    name = models.CharField(max_length=255, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    name = models.CharField(max_length=255, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    name = models.CharField(max_length=255, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.name


class ContentRating(models.Model):
    id = models.AutoField(primary_key=True) #explicit PK
    rating = models.CharField(max_length=15, unique=True) #unique constrain for integrity

    def __str__(self):
        return self.rating
    

class Movie(models.Model):
    id = models.AutoField(primary_key=True)  #explicit PK
    title = models.CharField(max_length=255) #not unique, movies may have identical titles
    director = models.ForeignKey(Director, on_delete=models.CASCADE)  #FK to Director
    duration = models.PositiveIntegerField()
    gross = models.BigIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)  #FK to Language
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  #FK to Country
    content_rating = models.ForeignKey(ContentRating, on_delete=models.CASCADE)  #FK to ContentRating
    budget = models.BigIntegerField()
    year = models.IntegerField()
    imdb_score = models.FloatField()
    actors = models.ManyToManyField(Actor, through='MovieActor')  #Many-to-Many relationship with Actor
    genres = models.ManyToManyField(Genre, through='MovieGenre')  #Many-to-Many relationship with Genre

    def __str__(self):
        return self.title
    

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  #FK to Movie
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)  #FK to Actor

    class Meta:
        unique_together = ('movie', 'actor')


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  #FK to Movie
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  #FK to Genre

    class Meta:
        unique_together = ('movie', 'genre')