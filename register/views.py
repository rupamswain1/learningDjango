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
            
            for i in range(0,10000):
                username=username+str(i)
                if User.objects.filter(username=username):
                    continue
                else:
                    break
                break
            messages.info(request, "Username "+tmp+ "is not available, try"+username+str(i))
            return redirect('register')
        else:
            if password==cnf_password:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"User Saved")
                return redirect('register')
            else:
                messages.info(request,"Confirm Password and Password is not matching")
                return redirect('register')
        

        
    else:
        return render(request,'register.html')
