from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    #router
    path('', include(router.urls))
]