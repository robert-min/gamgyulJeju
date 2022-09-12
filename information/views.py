from .models import *

from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404


# Create your views here.

def show_basic_info(request):
    return render(request, "information/about.html")

def show_family(request):
    families = FamilyDetail.objects.all()
    cur_detail = FamilyDetail.objects.get(slug="geugjosaeng")

    return render(request, "information/family.html", {'families': families, 'cur_detail': cur_detail})

def family_detail(request, family_slug=None):
    current_slug = None
    families = FamilyDetail.objects.all()
    cur_detail = FamilyDetail.objects.get(slug=family_slug)

    if family_slug:
        current_slug = get_object_or_404(FamilyDetail, slug=family_slug)

    return render(request, 'information/family.html', {'families': families, 'current_slug': current_slug, 'cur_detail': cur_detail})

def show_cultivation(request):
    cultivations = CultivationStatus.objects.all()
    return render(request, 'information/cultivation.html', {'cultivations': cultivations})

def show_health(request):
    return render(request, "information/health.html")