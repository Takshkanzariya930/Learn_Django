from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Hello, Welcome to Home Page.........</h1>")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("<h1>Hello, Welcome to About Page.........</h1>")

def contact(request):
    return HttpResponse("<h1>Hello, Welcome to Contact Page.........</h1>")