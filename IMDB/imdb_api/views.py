from django.shortcuts import render,HttpResponse
from .models import WatchList,StreamPlatform
# Create your views here.

def movie_list(request):
    movie_list=WatchList.objects.all()
    print(movie_list)
    return HttpResponse("testing movie list")


def movie_detail(request,pk):
    movie=WatchList.objects.get(pk=pk)
    print(movie)
    
    return HttpResponse("testing movie detail view")

