from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class CompanyViewSet (viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated,]