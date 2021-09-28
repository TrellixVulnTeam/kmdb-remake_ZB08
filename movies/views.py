from rest_framework import generics
from .models import Movie, Genre
from .serializers import MovieSerializer

class MovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

