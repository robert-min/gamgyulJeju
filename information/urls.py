from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "information"

urlpatterns = [
    path('', show_basic_info, name='info'),
    # path('family/', show_family, name='family'),
    path('family/<family_slug>/', family_detail, name='family_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)