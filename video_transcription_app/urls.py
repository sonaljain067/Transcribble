from django.urls import path 
from .views import transcibe_video 

urlpatterns = [
    path('video_transcribe', transcibe_video)
]