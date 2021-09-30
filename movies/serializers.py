from .models import Movie, Genre, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        genres_data = validated_data.pop('genres') # Faz a retirada dos generos para serem tratados a parte
        movie = Movie.objects.create(**validated_data) # Cria o filme na model

        for genre in genres_data: # Iteração sobre "genres_data"
            gen = Genre.objects.get_or_create(**genre)[0] # Pegando ou criando o gênero em questão
            movie.genres.add(gen) # Adicionando o genre ao movie, como se fosse um append 

        return movie


class FullMovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
