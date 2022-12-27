import email
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_view(request):
    # return HttpResponse("this is login page")
    if request.method=='POST':
        username=request.POST.get('username')
        
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            pass
        
        print(username,email,password,confirmpassword)

    return render(request,'account/signup.html')
