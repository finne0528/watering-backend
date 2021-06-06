from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('watering/init', csrf_exempt(views.create_watering_setting), name='create_watering_setting'),
    path('auto_watering/interval', csrf_exempt(views.update_auto_watering_interval), name='update_auto_watering_interval'),
]
