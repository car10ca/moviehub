from django.contrib import admin
from .models import Movie, Director, Actor, Genre, Language, Country, ContentRating

class MovieActorInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 1

class MovieGenreInline(admin.TabularInline):
    model = Movie.genres.through
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'imdb_score')
    list_filter = ('year', 'content_rating')
    search_fields = ('title', 'director__name')
    inlines = [MovieActorInline, MovieGenreInline]

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ContentRatingAdmin(admin.ModelAdmin):
    list_display = ('rating',)
    search_fields = ('rating',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(ContentRating, ContentRatingAdmin)
