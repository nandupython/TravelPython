from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import members

# Create your views here.
def sample(request):
    obj = place.objects.all()
    obj2 = members.objects.all()
    return render(request,'index.html',{'result1': obj,'result2':obj2})

#def new(request):
    #return render(request,'about.html')

