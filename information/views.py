from .models import *

from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404


# Create your views here.

def show_basic_info(request):
    return render(request, "information/home.html")

def show_family(request):
    return render(request, "information/family.html")

def family_detail(request, id, family_slug=None):
    family = get_object_or_404(FamilyDetail, id=id, slug=family_slug)
    return render(request, 'information/family.html', {'family': family})
