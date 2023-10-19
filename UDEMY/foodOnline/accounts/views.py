from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
from .models import User,UserProfile
from django.contrib import messages
from vendor.forms import VendorForm
from vendor.models import Vendor


def registerUser(request):
    if request.method=='POST':
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            # return redirect('registerUser')
        
        
            # Create the user using create_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            print('User is created')
            messages.success(request,"your acount has been registered successfully !")
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)

            
            
    else:
        
        form=UserForm()
    context={
        'form':form,
    }
    
    return render(request,'accounts/registerUser.html',context)
    # return HttpResponse("registerUSer page")
    
# def registerVendor(request):
#     if request.method =='POST':
#         # store the data and create the user
#         form=UserForm(request.POST)
#         v_form=VendorForm(request.POST,request.FILES)
#         if form.is_valid() and v_form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             username=form.cleaned_data['username']
#             email=form.cleaned_data['email']
#             password=form.cleaned_data['password']
#             user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
#             user.role=User.VENDOR
#             user.save()
#             vendor=v_form.save(commit=False)
#             vendor.user=user
#             user_profile=UserProfile.objects.get(user=user)
#             vendor.user_profile=user_profile
#             vendor.save()
#             message.success(request,"Your account has been registered sucesfully ! Please wait for the approval")
#             return redirect('registerVendor')
            
            
            
#         else:
#             print('invalid form')
#             print(form.errors)
#     else:
#         form=UserForm()
#         v_form=VendorForm()
#     context={
#         'form':form,
#         'v_form':v_form,
#     }
#     return render(request,'accounts/registerVendor.html',context)
    
def registerVendor(request):
    
    if request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor_name = v_form.cleaned_data['vendor_name']
            # vendor.vendor_slug = slugify(vendor_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
        else:
            print('invalid form')
            print(form.errors)
    else:
        form=UserForm()
        v_form=VendorForm()
        
    context={
        'form':form,
        'v_form':v_form,
    }
    return render(request,'accounts/registerVendor.html',context)

