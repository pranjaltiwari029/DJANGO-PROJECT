from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee


def home(request):
    # return HttpResponse("hello all")
    employees=Employee.objects.all()
    context={
        'employees':employees,
    }
    # print(employees)
    return render(request,'home.html',context)

def employee_detail(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    # return HttpResponse(employee)
    context={
        'employee':employee,
    }
    return render(request,'employee_detail.html',context)
        
    
        