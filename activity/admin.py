from django.contrib import admin
from .models import *
# Register your models here.

class show_activity(admin.ModelAdmin):
    list_display = ('id', 'place', 'how', 'website')

admin.site.register(ActivityMap, show_activity)
