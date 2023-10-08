from  django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('hello doston')
    return render(request,'home.html')