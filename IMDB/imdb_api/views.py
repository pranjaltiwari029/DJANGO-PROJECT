from django.http import HttpResponse,JsonResponse
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
from  rest_framework.response import Response
from rest_framework import status

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
    if request.method=='GET':
        stream_list=StreamPlatform.objects.all()
        serialized= StreamPlatformSerializer(stream_list,many= True)
        return JsonResponse(serialized.data,safe=False)
    
    elif request.method=='POST':
        _data=request.data
        serialized=StreamPlatformSerializer(data=_data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status= status.HTTP_201_CREATED)
        return Response(serialized.erros,status=status.HTTP_400_BAD_REQUEST)
            
            
            
def stream_detail(request,pk):
    stream_platform=StreamPlatform.objects.get(pk=pk)
    serialized=StreamPlatformSerializer(stream_platform)
    
    
    return JsonResponse(serialized.data)
