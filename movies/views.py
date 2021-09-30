from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import AdminPermission, CriticPermission, IsAdminCriticOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from .models import Movie
from .serializers import FullMovieSerializer, MovieSerializer


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

class RetrieveMovieView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminCriticOrReadOnly]

    def get_serializer_class(self): # Seleciona a classe do serializer de acordo com a condicional.
        if self.request.user.is_staff or self.request.user.is_superuser:
            return FullMovieSerializer
        return MovieSerializer

    