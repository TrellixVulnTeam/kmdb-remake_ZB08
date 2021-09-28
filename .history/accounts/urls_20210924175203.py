from django.urls import path
from .views import AccountView, LoginView

urlspatterns = [
    path('accounts/', AccountView.as_view()),
    path('login/', LoginView.as_view)
]