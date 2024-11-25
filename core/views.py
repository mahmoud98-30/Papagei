from django.contrib import messages
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, get_object_or_404, redirect
import os
from django.core.files.base import ContentFile

from io import BytesIO

from .forms import MediaFileForm
from .models import Transcribe
from .transcript import transcribe_audio
from .utils import ModelSizeChoices, LanguageChoices


def upload_media_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            media_file = form.save()
            audio = media_file.audio.url
            language = media_file.language
            model_size = form.cleaned_data.get('model_size', ModelSizeChoices.BASE)  # Fallback to default

            _, extension = os.path.splitext(audio)
            extension = extension.lower()
            if extension not in [ '.mp3', '.mp4', ]:
                messages.warning(request, 'Invalid file format. Supported formats are  MP3 and MP4.')
                return render(request, 'index.html', {'form': form, 'model_size_choices': ModelSizeChoices.choices, 'language': LanguageChoices.choices})

            try:
                # Get the transcription text
                transcription_text = transcribe_audio(audio, language, model_size)

                # Update the output_file and status fields in the Transcribe model
                media_file.output_file.save(
                    'transcription.txt',
                    ContentFile(transcription_text)
                )
                media_file.status = 'done'
                media_file.save()

                # Display a success message
                messages.success(request, 'Transcription completed successfully!')

                # Create response with the file content
                response = HttpResponse(transcription_text, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename="transcription.txt"'

                return response

            except Exception as e:
                # Update the status to failed in case of error
                media_file.status = 'failed'
                media_file.save()

                messages.error(request, f'Transcription error: {str(e)}')
                return render(request, 'index.html', {'form': form, 'model_size_choices': ModelSizeChoices.choices, 'language': LanguageChoices.choices})

        # Handle form validation errors
        messages.warning(request, f'{form.errors}')
        return render(request, 'index.html', {'form': form, 'errors': form.errors, 'model_size_choices': ModelSizeChoices.choices, 'language': LanguageChoices.choices})

    # For GET request, render the form
    form = MediaFileForm()
    return render(request, 'index.html', {'form': form, 'model_size_choices': ModelSizeChoices.choices, 'language': LanguageChoices.choices})



def support(request):
    return render(request, 'support.html')


def list_files(request):
    files  = Transcribe.objects.all()
    context = {'files': files}
    return render(request, 'media_files.html', context)

def delete_file(request, pk):
    file = get_object_or_404(Transcribe, pk=pk)
    if request.method == "POST":
        file.delete()
        messages.success(request, "File deleted successfully.")
        return redirect('list_files')  # Replace with your list view name
    return redirect('list_files')