from django.contrib import admin
from .models import FamilyDetail
# Register your models here.

class show_family(admin.ModelAdmin):
    list_display = ('id', 'eng_title', 'kor_title', 'slug')

admin.site.register(FamilyDetail, show_family)
