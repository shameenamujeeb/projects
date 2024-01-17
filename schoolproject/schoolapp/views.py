from django.shortcuts import render
from . models import Programs


# Create your views here.
def home(request):
    pgm=Programs.objects.all()
    return render(request,'index.html',{'obj':pgm})


