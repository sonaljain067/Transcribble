import requests
from .models import Video
from django.shortcuts import render 
from django.core.files.storage import default_storage 
from django.views.decorators.csrf import csrf_exempt
from pydub import AudioSegment
import speech_recognition as sr 

@csrf_exempt
def transcibe_video(request):
    if request.method == 'POST': 
        video_url = request.POST.get('video_url')
        
        # 1. Download video
        video_file = default_storage.open('temp_video.mp4', 'wb')
        video_file.write(requests.get(video_url).content)
        video_file.close()

        # 2. Convert video to audio
        audio_file = default_storage.open('temp_audio.wav', 'wb')
        audio = AudioSegment.from_file('temp_video.mp4')
        audio.export(audio_file, format='wav')
        audio_file.close()

        # 3. Transcribe audio
        audio_file = default_storage.open('temp_audio.wav', 'rb')
        r = sr.Recognizer()
        audio_file = AudioSegment.from_file('temp_audio.wav')
        start_time = 4500
        end_time = 70000

        audio_segment = audio_file[start_time:end_time]
        audio_segment.export('temp.wav', format = 'wav')
        audio = sr.AudioFile('temp.wav')
        with audio as source:
            audio = r.record(source)
            try:
                transcript = r.recognize_google(audio)
            except Exception as e:
                print(e)
          
        # 4. Save video information and transcript to database
        # video = Video(video_url=video_url, transcript=transcript)
        # video.save()

        # 5. Render template with transcription result
        return render(request, 'transcription_result.html', {'transcript': transcript})

    return render(request, 'transcribe_video.html')