from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "best"

urlpatterns = [
    path('', show_best_pick, name='best_pick'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)