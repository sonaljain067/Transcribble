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
        r = sr.Recognizer()
        audio_file = AudioSegment.from_file('temp_audio.wav')
        from pydub.utils import make_chunks
        chunk_size_ms = 10000
        transcript = ''
        chunks = make_chunks(audio_file, chunk_size_ms)
        for i, chunk in enumerate(chunks):
            chunk_name = f"chunk{i}.wav"
            chunk.export(chunk_name, format="wav")
            with sr.AudioFile(chunk_name) as source:
                audio = r.record(source)
                try: 
                    chunk_transcript = r.recognize_google(audio)
                except Exception as e: 
                    print(e)
                    chunk_transcript = ''
                transcript += chunk_transcript

        # 4. Save video information and transcript to database
        video = Video(video_url=video_url, transcript=transcript)
        video.save()

        # 5. Render template with transcription result
        return render(request, 'transcription_result.html', {'transcript': transcript})

    return render(request, 'transcribe_video.html')