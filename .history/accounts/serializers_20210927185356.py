from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_active', 'date_joined', 'email', 'groups', 'user_permissions']
    
    def create(self, validated_data):
        