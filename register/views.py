from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        cnf_password=request.POST['password2']
        tmp=username
        if User.objects.filter(username=username):
            suggestName=first_name+last_name
            
            for i in range(0,10000):
                username=suggestName+str(i)
                print(username)
                print(User.objects.filter(username=username))
                if User.objects.filter(username=username):
                    print(True)
                    pass
                else:
                    break
                
            print(username)
            messages.info(request, "Username "+tmp+ " is not available, try "+username)
            return redirect('register')
        else:
            if password==cnf_password:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"User Saved")
                return redirect('login')
            else:
                messages.info(request,"Confirm Password and Password is not matching")
                return redirect('register')
        

        
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "user name orpp password incorrect")
            return render(request,'login.html')
    else:
         return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


   
