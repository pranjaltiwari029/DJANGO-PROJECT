from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
    # path('list/',views.movie_list,name="movie-list"),
    # path('list/<int:pk>',views.movie_detail,name='movie-detail'),
     path('stream/',views.StreamPlatformList.as_view(),name='stream-platform'),
    path('stream/<int:pk>',views.StreamPlatformDetail.as_view(),name='stream-platform-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
