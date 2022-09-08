from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "activity"

urlpatterns = [
    path('', show_activity, name='activity'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)