from django.urls import path
from .views import MovieView, RetrieveMovieView, ReviewView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/review/', ReviewView.as_view()),
    path('movies/<int:movie_id>/', RetrieveMovieView.as_view()),
    path('movies/<int:movie_id>/review/', ReviewView.as_view()),
]
