from .models import *

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


# Create your views here.

def show_activity(request):
    activities = ActivityMap.objects.all()
    return render(request, "activity/activity.html", {"activities": activities})