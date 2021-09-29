from django.urls import path
from .views import MovieView, RetrieveMovieView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', RetrieveMovieView.as_view())
]