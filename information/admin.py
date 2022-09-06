from django.contrib import admin
from .models import *
# Register your models here.

class show_family(admin.ModelAdmin):
    list_display = ('id', 'eng_title', 'kor_title', 'slug')

class show_cultivation(admin.ModelAdmin):
    list_display = ('id', 'eng_title', 'kor_title' )

admin.site.register(FamilyDetail, show_family)
admin.site.register(CultivationStatus, show_cultivation)
