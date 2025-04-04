from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
 
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/admin')  
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, "users/login.html")