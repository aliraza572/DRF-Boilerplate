from django.shortcuts import render
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

from django.contrib.gis.geoip2 import GeoIP2

from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .utils import *


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated,]

    @transaction.atomic
    def create(self, request, *args, **kwargs):

        # '''
        payload = {
            "user" : {
                "first_name" : "Jhon",
                "last_name" : "Doe",
                "username" : "jhondoe",
                "email" : "jhondoe@mail.com",
                "password" : "123@124mypass"
            },
            "gender": "MALE",
            "company" : 1,
        }
        # '''
        user_serializer = UserSerializer(data=request.data.pop('user'))
        profile_serializer = UserProfileSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True) and profile_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

            try:
                ip_address = get_client_ip(request)
                g = GeoIP2()
                location_info = g.city(ip_address)
                profile_serializer.validated_data['geolocation'] = location_info.get('city', '')
            except Exception as e:
                # Handle exceptions, such as unable to retrieve geolocation data
                pass

            # Create user profile
            profile_serializer.validated_data['user'] = user
            profile = profile_serializer.save()

            return Response(UserProfileSerializer(profile).data, status=status.HTTP_201_CREATED)