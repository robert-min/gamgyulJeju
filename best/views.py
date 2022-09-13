from .models import *

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


# Create your views here.


def show_best_pick(request):
    return render(request, "best/pick.html")