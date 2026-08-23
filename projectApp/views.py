from django.shortcuts import render

def home(request):
    return render(request, 'projectApp/home.html')