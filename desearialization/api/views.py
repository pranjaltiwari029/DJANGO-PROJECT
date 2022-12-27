from django.shortcuts import render

# Create your views here.
from io import BytesIO 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serialiser import StudentSerialiser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def createStudentData(request):
    if request.method == 'POST':
        json_data = request.body 
        # it converted the json data into stream data 
        byteStream = BytesIO(json_data)
        # it converted stream data into python data            
        pythonData = JSONParser().parse(byteStream)
        # it converted python data into complex data type 
        serialisedData = StudentSerialiser(data = pythonData)

        if serialisedData.is_valid():
            serialisedData.save()
            response = {
                'message' : 'Your data is saved successfully!!'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialisedData.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    return HttpResponse('This is a get request')
    