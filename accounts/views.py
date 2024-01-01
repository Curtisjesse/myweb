from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    return render(request, 'register.html')

def sign_up(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        user = User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, second_name=second_name)
        user.save();
        print('user created')
        return redirect('/')
    else:      
        return render(request, 'sign_up.html')
# Create your views here.
