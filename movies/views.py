from rest_framework import generics, status
from rest_framework.response import Response
from .permissions import AdminPermission, CriticPermission, IsAdminCriticOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from .models import Movie, Review
from .serializers import FullMovieSerializer, MovieSerializer, ReviewSerializer
import ipdb

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
        if self.request.user.is_authenticated:
            return FullMovieSerializer
        return MovieSerializer

class ReviewView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'movie_id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [CriticPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Desenvolver a lógica que atenda os requisitos propostos

        # TODO Verificar se já existe uma review associada ao crítico, se o movie_id é valido
        review = Review.objects.filter(critic=request.user.id, movie=kwargs['movie_id']) 
        movie = get_object_or_404(Movie, pk=kwargs['movie_id'])

        # TODO se não existir criar essa review
        if len(review) == 0:
            # Passar a response para o ReviewSerializer
            create_review = Review.objects.create(**request.data, critic=request.user, movie=movie)
            serializer = ReviewSerializer(create_review)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # ! Se já existir retornar uma mensagem padrão do material
        return Response({"detail": "You already made this review."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False) #PARTIAL FALSE == PUT PARTIAL TRUE==PATCH
        review = get_object_or_404(Review, critic=request.user.id, movie=kwargs['movie_id']) # VERIFICANDO SE A REVIEW EXISTE E INSTANCIANDO
        serializer = self.get_serializer(review, data=request.data, partial=partial) # SERIALIZANDO A REVIEW
        serializer.is_valid(raise_exception=True) # VERIFICANDO SE O SERIALIZER É VALIDO

        self.perform_update(serializer) # FAZENDO E SALVANDO AS ALTERAÇÕES PROPOSTAS

        return Response(serializer.data) # RETORNANDO SERIALIZER DATA, COM HTTP RESPONSE 200 (PADRÃO)


