from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,f'Invalid login')
            return redirect("login")
    else:    
        return render(request, "login.html")
    
def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if password == cpassword:
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            else :
                return redirect('signup')   
        else:
            return render(request, "signup.html")
    except:
        messages.info(request, "Username is already exists.")
        return render(request, 'signup.html')
    
def home(request):
    return render(request, "home.html")

def logout(request):
    auth.logout(request)    
    return redirect('home')


    


