"""ClassBasedAPIView URL Configuration

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
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lc/', views.LCStudentData.as_view(), name='lc'),
    path('rud/<int:pk>', views.RUDStudentData.as_view(), name='rud'),
    # path('view/', views.StudentData.as_view(), name='view'),
    # path('view/<int:pk>/', views.StudentRetrieve.as_view(), name='viewperrecord'),
    # path('create/', views.StudentCreate.as_view(), name='create'),
    # path('update/<int:pk>', views.StudentUpdate.as_view(), name='update'),
    # path('del/<int:pk>', views.StudentDel.as_view(), name='del'),
    
]
