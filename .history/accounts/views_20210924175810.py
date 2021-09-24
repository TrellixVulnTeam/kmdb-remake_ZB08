from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
class AccountView(generics.CreateAPIView):
    queryset = User.objects.all()
    