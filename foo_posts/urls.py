from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('foo_post', FooPostViewSet, basename='foo_post')

urlpatterns = [
    path('', include(router.urls)),
]
