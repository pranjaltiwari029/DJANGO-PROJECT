from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    data={
        'emps':emps
    }
    return render(request,'all_emp.html',data)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        bonus=int(request.POST['bonus'])
        
        
        new_emp=Employee(first_name=first_name,last_name =last_name,salary =salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()  
         
        return HttpResponse("employee Added succssfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Ocured! ")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
        except:
            return HttpResponse("Pleae enter a valid ID")
    
    emps=Employee.objects.all()
    data={
        'emps': emps
    }
    return render(request,'remove_emp.html',data)

def filter_emp(request):
    return render(request,'filter_emp.html')