
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>',views.student),
    path('student/',views.allStudent)
]
