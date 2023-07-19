from django.shortcuts import render,HttpResponse

# Create your views here.

def movie_list(request):
    return HttpResponse("Testing list view")

def movie_detail(request,pk):
    
    return HttpResponse("testing movie detail view")

