from django.shortcuts import render
from .models import Student
from .serialiser import StudentSerialiser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
#fetching data of all the students
def allStudent(request):
    s= Student.objects.all()
    serialsedData = StudentSerialiser(s)
    jsonData = JSONRenderer().render(serialsedData.data)
    return HttpResponse(jsonData,content_type = 'application/json')

    

def student(request,slug):
    s = Student.objects.get(id = slug)
    # python me convert ho gaya
    serialisedData = StudentSerialiser(s)
    # python to json me convert
    jsonData = JSONRenderer().render(serialisedData.data)
    return HttpResponse(jsonData,  content_type = 'application/json')



