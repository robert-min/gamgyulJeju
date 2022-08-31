from django.shortcuts import render

# Create your views here.

def show_basic_info(request):
    return render(request, "information/home.html")

def show_family(request):
    return render(request, "information/family.html")