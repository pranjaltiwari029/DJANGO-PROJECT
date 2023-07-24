from django.http import HttpResponse,JsonResponse
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
# Create your views here.

def movie_list(request):
    movie_list=WatchList.objects.all()
    serialized= WatchListSerializer(movie_list,many= True)
    return JsonResponse(serialized.data,safe=False)


def movie_detail(request,pk):
    movie=WatchList.objects.get(pk=pk)
    serialized=WatchListSeriallizer(movie)
    
    
    return JsonResponse(serialized.data)

def stream_list(request):
    stream_list=StreamPlatform.objects.all()
    serialized= StreamPlatformSerializer(stream_list,many= True)
    return JsonResponse(serialized.data,safe=False)

def stream_detail(request,pk):
    stream_platform=StreamPlatform.objects.get(pk=pk)
    serialized=StreamPlatformSerializer(stream_platform)
    
    
    return JsonResponse(serialized.data)
