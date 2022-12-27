from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('article_page')
    else:
        form = UserCreationForm()
    data = {
        'form' : form
    }
    return render(request, 'signup.html', data)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            url = None 
            url = request.POST.get('next')
            if url is not None: 
                return redirect(url)
            return redirect('article_page')
    else: 
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('signuppage')

