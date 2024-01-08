from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
    def validate_email(self, value):
        """
        Validate that the email address is in the correct format.
        """
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError('Enter a valid email address.')

        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data            
        )
        user.set_password(validated_data['password'])
        return user