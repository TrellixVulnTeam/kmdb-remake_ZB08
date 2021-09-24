from django.urls import path
from .views import AccountView

urlspatterns = [
    path('accounts/', AccountView.as_view()),
    path('login/', LoginView.as_view())
]