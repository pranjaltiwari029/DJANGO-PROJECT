from django.http import HttpResponse
from  django.shortcuts import render

def home(request):
    # return HttpResponse("hello")
    return render(request,"home-todo.html")