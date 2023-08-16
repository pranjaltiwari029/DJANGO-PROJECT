from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'stream', views.StreamPlatformViewSet,basename="streamplatform")



urlpatterns = [
    
    path('list/',views.movie_list,name="watchlist-list"),
    path('list/<int:pk>/',views.movie_detail,name='watchlist-detail'),
    path('list/<int:pk>/review/',views.ReviewListView.as_view(),name='review-view'),
    path('list/<int:pk>/review-create/',views.ReviewCreate.as_view(),name='review-create'),
    path('list/review/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    
    # path('reviews/',views.ReviewListView.as_view(),name='review-view'),
    # path('reviews/<int:pk>',views.ReviewDetailView.as_view(),name='review-detail'),
    path('', include(router.urls)),
    path('',views.api_root),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

