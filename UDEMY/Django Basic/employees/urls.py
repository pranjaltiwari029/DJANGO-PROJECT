from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('employees/<int:pk>/',views.employee_detail,name="employee_detail"),
]