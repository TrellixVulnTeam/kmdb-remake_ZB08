from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    model = User
    exclude = ['last_login', 'is_active', 'date_joined', 'email', 'groups', 'user_permissions']