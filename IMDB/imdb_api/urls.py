from django.urls import path,include
from . import views

urlpatterns = [
    
    path('list/',views.movie_list,name="movie-list"),
    path('list/<int:pk>',views.movie_detail,name='movie-detail'),
    path('stream/',views.stream_list,name='stream-platform'),
    path('stream/<int:pk>',views.stream_detail,name='stream-platform-detail'),
]
