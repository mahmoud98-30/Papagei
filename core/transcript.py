import os
from django.http import HttpResponse
from faster_whisper import WhisperModel


def transcribe_audio(audio_path,language,model_size):
        current_path = os.getcwd()
        fixed_path = audio_path.lstrip('/')
        audio_path = os.path.join(current_path, fixed_path)

        try:
            model = WhisperModel(model_size, device="cpu")
            segments, info = model.transcribe(audio_path, beam_size=5, language=language,
                                              condition_on_previous_text=False)

            # Prepare text content with timestamps
            transcript_lines = []
            for segment in segments:
                line = "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
                transcript_lines.append(line)

            # Join the lines into a single text
            transcript_content = "\n".join(transcript_lines)


            return transcript_content

        except Exception as e:
            return HttpResponse(f"Error during transcription: {str(e)}", status=500)



