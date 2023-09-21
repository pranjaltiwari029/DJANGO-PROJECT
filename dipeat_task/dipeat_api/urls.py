from django.urls import path,include
from . import views

urlpatterns = [
    
    path('login/',views.login_api,name="login_api"),
    path('user/',views.user_data,name="user_data"),
    path('register/',views.register_api,name="register_api"),
]
