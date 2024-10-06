from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Count, F, Sum, Q, Avg
from .models import Movie, Director, Actor, MovieActor, ContentRating, Language, Genre
from .forms import MovieForm

def frontend_home_view(request):
    #render the frontend homepage
    return render(request, 'movies/home.html')



#========================== MOVIES ==========================

def movie_list(request):
    #get sorting, ordering, initial letter, and search query parameters from the request
    sort_by = request.GET.get('sort', 'title')
    order = request.GET.get('order', 'asc')
    initial = request.GET.get('initial', None)
    search_query = request.GET.get('q', '')

    #sort the movies based on the parameters
    if sort_by == 'title':
        movies = Movie.objects.order_by('-title') if order == 'desc' else Movie.objects.order_by('title')
    else:
        movies = Movie.objects.all()
    
    #filter movies by initial letter if provided
    if initial:
        movies = movies.filter(title__istartswith=initial)
    
    #filter movies by search query if provided
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    return render(request, 'movies/movie_list.html', {'movies': movies, 'sort_by': sort_by, 'order': order, 'initial': initial, 'search_query': search_query})

def movie_detail(request, pk):
    #get a single movie by primary key and render its detail view
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_create(request):
    #create a new movie using a form
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_update(request, pk):
    #update an existing movie using a form
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_delete(request, pk):
    #delete an existing movie
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})

def top_grossing_movies_view(request):
    #render the top grossing movies view
    return render(request, 'movies/top_grossing_movies.html')

def top_movies_by_imdb(request):
    #order movies by IMDb score in descending order and limit to the top 10
    movies = Movie.objects.order_by('-imdb_score')[:10]
    return render(request, 'movies/top_movies_by_imdb.html', {'movies': movies})


def movies_by_year_genre(request):
    #filter movies by year and genre
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    genres = Genre.objects.all()
    
    selected_year = request.GET.get('year')
    selected_genre = request.GET.get('genre')

    movies = Movie.objects.all()
    if selected_year:
        movies = movies.filter(year=selected_year)
    if selected_genre:
        movies = movies.filter(genres__name=selected_genre)

    return render(request, 'movies/movies_by_year_genre.html', {
        'years': years,
        'genres': genres,
        'movies': movies,
        'selected_year': selected_year,
        'selected_genre': selected_genre,
    })



def movies_by_content_rating(request):
    #filter movies by content rating
    content_ratings = ContentRating.objects.all()
    
    selected_rating = request.GET.get('rating')

    movies = Movie.objects.all()
    if selected_rating:
        movies = movies.filter(content_rating__rating=selected_rating)

    return render(request, 'movies/movies_by_content_rating.html', {
        'content_ratings': content_ratings,
        'movies': movies,
        'selected_rating': selected_rating,
    })


def movies_by_language(request):
    #filter movies by language
    languages = Language.objects.all()
    
    selected_language = request.GET.get('language')

    movies = Movie.objects.all()
    if selected_language:
        movies = movies.filter(language__name=selected_language)

    return render(request, 'movies/movies_by_language.html', {
        'languages': languages,
        'movies': movies,
        'selected_language': selected_language,
    })




#========================== DIRECTORS ==========================
def directors_list(request):
    #get sorting, ordering, initial letter, and search query parameters from the request
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')
    initial = request.GET.get('initial', None)
    search_query = request.GET.get('q', '')

    #sort the directors based on the parameters
    if sort_by == 'name':
        directors = Director.objects.order_by('-name') if order == 'desc' else Director.objects.order_by('name')
    else:
        directors = Director.objects.all()
    
    #filter directors by initial letter if provided
    if initial:
        directors = directors.filter(name__istartswith=initial)
    
    #filter directors by search query if provided
    if search_query:
        directors = directors.filter(name__icontains=search_query)

    return render(request, 'movies/directors_list.html', {'directors': directors, 'sort_by': sort_by, 'order': order, 'initial': initial, 'search_query': search_query})

def top_directors(request):
    #aggregate the total gross earnings for each director and sort them in descending order
    directors = Director.objects.annotate(total_gross=Sum('movie__gross')).order_by('-total_gross')[:10]
    return render(request, 'movies/top_directors.html', {'directors': directors})

def top_versatile_directors(request):
    #annotate each director with the count of unique actors they've worked with
    directors = Director.objects.annotate(
        unique_actors=Count('movie__movieactor__actor', distinct=True)
    ).order_by('-unique_actors')[:5]
    return render(request, 'movies/top_versatile_directors.html', {'directors': directors})

def top_directors_by_imdb_view(request):
    #calculate the average IMDb score for each director's movies and return the top 10 directors
    directors = Director.objects.annotate(average_imdb=Avg('movie__imdb_score')).order_by('-average_imdb')[:10]
    return render(request, 'movies/top_directors_by_imdb.html', {'directors': directors})




#========================== ACTORS ==========================
def actors_list(request):
    #get sorting, ordering, initial letter, and search query parameters from the request
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')
    initial = request.GET.get('initial', None)
    search_query = request.GET.get('q', '')

    #sort the actors based on the parameters
    if sort_by == 'name':
        actors = Actor.objects.order_by('-name') if order == 'desc' else Actor.objects.order_by('name')
    else:
        actors = Actor.objects.all()
    
    #filter actors by initial letter if provided
    if initial:
        actors = actors.filter(name__istartswith=initial)
    
    #filter actors by search query if provided
    if search_query:
        actors = actors.filter(name__icontains=search_query)

    return render(request, 'movies/actors_list.html', {'actors': actors, 'sort_by': sort_by, 'order': order, 'initial': initial, 'search_query': search_query})

def actors_with_director_view(request):
    #render the actors with director view
    return render(request, 'movies/actors_with_director.html')



def movies_by_actor(request):
    #filter: select an actor and see all movies they're in
    actors = Actor.objects.all()
    
    selected_actor = request.GET.get('actor')

    movies = Movie.objects.all()
    if selected_actor:
        movies = movies.filter(actors__name=selected_actor)

    return render(request, 'movies/movies_by_actor.html', {
        'actors': actors,
        'movies': movies,
        'selected_actor': selected_actor,
    })

