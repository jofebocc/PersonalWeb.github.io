from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")

def pdf_view(request):
    pdf_path = 'static/core/img/Resume_updated.pdf'
    return render(request, 'core/home.html', {'pdf_path': pdf_path})