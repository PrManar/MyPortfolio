from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def certifications(request):
    return render(request, 'certifications.html')

def contact(request):
    return render(request, 'contact.html')
