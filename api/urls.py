from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('auto_watering/interval', csrf_exempt(views.update_auto_watering_interval), name='update_auto_watering_interval'),
]
