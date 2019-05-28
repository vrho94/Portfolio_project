from django.shortcuts import render
from .models import Job#pomeni da prenesemo model te aplikacije v views

def Home(request):
    jobs=Job.objects#definiramo novo spremenljivko kamor zapišemo naš model
    #nato to spremenljivko priredimo kot tretji argument list jobs funkcije render
    return render(request, 'jobs/home.html', {'jobs':jobs})
