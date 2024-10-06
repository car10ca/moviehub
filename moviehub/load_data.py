import csv
import os
import django

#set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviehub.settings')
django.setup()

#import models from movies app (tables to store data)
from movies.models import Movie, Director, Actor, Genre, Language, Country, ContentRating, MovieActor, MovieGenre

def load_data(file_path):
    #dictionary mapping: internal fields to actual column names in csv
    required_fields = {
        'director_name': 'director_name',
        'language': 'language',
        'country': 'country',
        'content_rating': 'content_rating',
        'movie_title': 'movie_title',
        'duration': 'duration',
        'gross': 'gross',
        'budget': 'budget',
        'year': 'title_year',
        'imdb_score': 'imdb_score',
        'actor_1_name': 'actor_1_name',
        'actor_2_name': 'actor_2_name',
        'actor_3_name': 'actor_3_name',
        'genres': 'genres'
    }
    #open csv file in read mode using dictreader 
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        #prints csv headers for debugging (read issues during first load attempt)
        print("CSV Headers:", reader.fieldnames)

        #iterate over each row and check that required fields are present and not empty
        for i, row in enumerate(reader):
            try:
                # Only process rows that have all required fields
                if all(field in row and row[field].strip() != '' for field in required_fields.values()):
                    #extract and clean required data for each row
                    #remove whitespace
                    #convert numerical fields (duration, gross, etc) into appropriate types
                    #split genre field into list of genres using split |
                    director_name = row[required_fields['director_name']].strip()
                    language = row[required_fields['language']].strip()
                    country = row[required_fields['country']].strip()
                    content_rating = row[required_fields['content_rating']].strip()
                    movie_title = row[required_fields['movie_title']].strip()
                    duration = int(row[required_fields['duration']].strip())
                    gross = int(row[required_fields['gross']].strip())
                    budget = int(row[required_fields['budget']].strip())
                    year = int(row[required_fields['year']].strip())
                    imdb_score = float(row[required_fields['imdb_score']].strip())
                    actor_1_name = row[required_fields['actor_1_name']].strip()
                    actor_2_name = row[required_fields['actor_2_name']].strip()
                    actor_3_name = row[required_fields['actor_3_name']].strip()
                    genres = row[required_fields['genres']].strip().split('|')

                    print(f"Processing row {i}: {movie_title}, {director_name}, {year}")

                    #create or get Director, Language, Country, ContentRating instances
                    director, _ = Director.objects.get_or_create(name=director_name)
                    language, _ = Language.objects.get_or_create(name=language)
                    country, _ = Country.objects.get_or_create(name=country)
                    content_rating, _ = ContentRating.objects.get_or_create(rating=content_rating)

                    #create Movie instance and save to database
                    movie = Movie(
                        title=movie_title,
                        director=director,
                        duration=duration,
                        gross=gross,
                        language=language,
                        country=country,
                        content_rating=content_rating,
                        budget=budget,
                        year=year,
                        imdb_score=imdb_score
                    )
                    movie.save()
                    print(f"Saved movie: {movie.title}")

                    # Create or get Actor instances and create many-to-many relationships
                    actor_1, _ = Actor.objects.get_or_create(name=actor_1_name)
                    actor_2, _ = Actor.objects.get_or_create(name=actor_2_name)
                    actor_3, _ = Actor.objects.get_or_create(name=actor_3_name)

                    MovieActor.objects.create(movie=movie, actor=actor_1)
                    MovieActor.objects.create(movie=movie, actor=actor_2)
                    MovieActor.objects.create(movie=movie, actor=actor_3)
                    print(f"Created actors: {actor_1_name}, {actor_2_name}, {actor_3_name}")

                    #split genre string into individual genres
                    #create Genre instances and create many-to-many relationships
                    for genre_name in genres:
                        genre, _ = Genre.objects.get_or_create(name=genre_name.strip())
                        MovieGenre.objects.create(movie=movie, genre=genre)
                    print(f"Created genres: {genres}")

            #catch and print exceptions: skip rows that cause exceptions and continue with next row
            except (KeyError, ValueError) as e:
                print(f"Skipping row {i} due to error: {e}")
                print(f"Row {i} data: {row}")
                continue
#set filepath to csv file and call function
if __name__ == "__main__":
    file_path = '/Users/kerstinkegel/Documents/CM3035AWD/midTerm/moviehub/movie_data.csv'
    load_data(file_path)
