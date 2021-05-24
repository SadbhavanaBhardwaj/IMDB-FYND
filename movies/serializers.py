from rest_framework import serializers

from movies.models import Movie, Rating, Genre
from users.models import ImdbUser


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    class Meta:
        model = Genre
        fields = ['name']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
    def save(self):
        data = self.validated_data
        try:
            rating_obj = Rating.objects.get(user=data['user'], movie=data['movie'])
            rating_obj.score = data['score']
            rating_obj.save()
        except Exception:
            rating_obj = Rating.objects.create(score=data['score'], user=data['user'], movie=data['movie'])
        
        return rating_obj

class MovieListSerializer(serializers.ModelSerializer):
    """
        serializer for listing the movies
    """
    imdb_score = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()

    def get_genre(self, instance):
        genre = list(Genre.objects.filter(movie__in=[instance]).values_list('name', flat=True))
        return genre

    def get_imdb_score(self, instance):
        rating = list(Rating.objects.filter(movie=instance).values_list('score', flat=True))
        total_users = len(rating)
        try:
            return sum(rating)/total_users
        except Exception:
            return 0
    class Meta:
        model = Movie
        fields = ['name', 'director', "popularity", 'genre', 'imdb_score']


class MovieSerializer(serializers.ModelSerializer):
    """
        serializer for create, update and delete movie
    """    
    class Meta:
        model = Movie
        fields = ['name', 'director', "popularity", 'genre']