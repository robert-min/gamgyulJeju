from django.urls import path
from .views import *

app_name = "information"

urlpatterns = [
    path('', show_basic_info, name='tool_all'),
]