from django.shortcuts import render
from .models import Destination
# Create your views here.
def travelHome(request):
    
    dest=Destination.objects.all()
    return render(request,'index.html',{'dest':dest})