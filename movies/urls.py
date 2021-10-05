from django.urls import path
from .views import MovieView, RetrieveMovieView, ReviewView, SpecificReviewView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('reviews/', SpecificReviewView.as_view()),
    path('movies/<int:movie_id>/', RetrieveMovieView.as_view()),
    path('movies/<int:movie_id>/review/', ReviewView.as_view()),
]
