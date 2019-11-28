from django.shortcuts import render
from .models import Project
# Create your views here.

def portafolio(request):
    projetcs = Project.objects.all()
    return render(request, "portafolio/portafolio.html",{'projects':projetcs})