from django.urls import path,include
from . import views

urlpatterns = [
    
    path('list/',views.movie_list,name="movie-list"),
    path('list/<int:pk>',views.movie_detail,name='movie.detail'),
]
