"""JWTAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView, TokenVerifyView
from app1 import views
#router = DefaultRouter()
#router.register('StudentModelViewSet', views.StudentModelViewSet, basename='StudentModelViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lc/', views.LCStudent.as_view(), name='lc'),
    path('rud/<int:pk>', views.RUDStudent.as_view(), name='rud'),
    #path('', include(router.urls)),
    #path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
