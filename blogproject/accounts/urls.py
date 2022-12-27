

from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup_view,name="signuppage"),
    path('login/',views.login_view),
    path('logout/',views.logout_view)
]
