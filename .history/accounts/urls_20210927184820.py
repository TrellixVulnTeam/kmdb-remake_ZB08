from django.urls import path
from .views import AccountView

urlpatterns = [
    path('accounts/', AccountView.as_view()),
    path('login/', AccountView.as_view()),

]