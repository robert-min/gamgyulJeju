from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "best"

urlpatterns = [
    path('', show_best_pick, name='best_pick'),
    path('keep/', show_best_keep, name='best_keep'),
    path('food/', show_best_food, name='best_food')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)