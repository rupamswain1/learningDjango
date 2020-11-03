from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        print("saved")
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        cnf_password=request.POST['password1']
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print("saved")
        #return redirect('/')
    else:
        return render(request,'register.html')
