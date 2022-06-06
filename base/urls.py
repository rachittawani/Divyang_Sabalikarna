from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tts/', views.tts, name="tts"),
    path('stt/', views.stt, name="stt"),
]