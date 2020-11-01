from django.shortcuts import render
from .models import Destination
# Create your views here.
def travelHome(request):
    dest1=Destination()
    dest2=Destination()
    dest1.name='Bhubaneswar'
    dest1.price="200"
    dest1.image="index-01.jpg"
    dest2.name='Puri'
    dest2.price='300'
    dest2.image="index-02.jpg"
    dest3= Destination()
    dest3.name="Cuttack"
    dest3.price="500"
    dest3.image="index-03.jpg"
    dest=[dest1,dest2,dest3]

    return render(request,'index.html',{'dest':dest})