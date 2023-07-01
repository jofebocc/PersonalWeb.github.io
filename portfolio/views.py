from django.shortcuts import render
from portfolio.models import Project
# Create your views here.

def portfolio(request):
    proyectos = Project.objects.all()
    return render(request, "portfolio/portfolio.html" , {'proyectos' : proyectos})
