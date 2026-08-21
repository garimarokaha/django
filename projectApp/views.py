from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Website</h1>")
def  about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of the website.</p>")