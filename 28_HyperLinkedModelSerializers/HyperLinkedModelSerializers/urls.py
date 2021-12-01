from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from app1 import views
router = DefaultRouter()
#router.register('StudentModelViewSet', views.PlayerAPI, basename='StudentModelViewSet')
router.register('StudentModelViewSet', views.PlayerAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls')),
]
