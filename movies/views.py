from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from .models import Movie, Genre
from .serializers import MovieSerializer, MovieRetrieveSerializer


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

class RetrieveMovieView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'