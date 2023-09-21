from django.urls import path,include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('user',UserViewSet,basename='user')
urlpatterns = [
    # path('', include(router.urls)),
    path('user5/',views.UserViewSet,name="userviewset"),
    
    
]
