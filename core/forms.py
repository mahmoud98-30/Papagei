import os
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django import forms
from .models import Transcribe
from .utils import convert_to_mp3, ModelSizeChoices


class MediaFileForm(forms.ModelForm):
    model_size = forms.ChoiceField(choices=ModelSizeChoices.choices, required=False, initial=ModelSizeChoices.BASE)

    class Meta:
        model = Transcribe
        fields = ['title', 'language', 'model_size', 'audio']

    def clean_audio(self):
        file = self.cleaned_data.get('audio')

        if not file:
            raise forms.ValidationError("No file uploaded.")

        # Check file extension
        file_extension = os.path.splitext(file.name)[1].lower()
        if file_extension == '.mp4':
            # Save the uploaded file temporarily for validation and processing
            temp_path = f"uploads/video/{file.name}"
        else:
            temp_path = f"uploads/audio/{file.name}"

        current_path = os.getcwd()
        # Create full file path by joining current path and filename
        file_path = os.path.join(current_path, temp_path)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save the original file
        with open(file_path, 'wb') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        try:
            if file_extension == '.mp4':
               processed_file_path = convert_to_mp3(file_path)
            else:
                processed_file_path = file_path
            # Create a new InMemoryUploadedFile with the processed MP3
            with open(processed_file_path, 'rb') as mp3_file:
                file_content = mp3_file.read()
                file_name = os.path.basename(processed_file_path)
                file = InMemoryUploadedFile(
                    file=io.BytesIO(file_content),
                    field_name='audio',
                    name=file_name,
                    content_type='audio/mpeg',
                    size=len(file_content),
                    charset=None
                )

            # Clean up: Delete both temporary files
            os.remove(file_path)  # Delete original file


        except Exception as e:
            # Clean up the original file in case of error
            if os.path.exists(file_path):
                os.remove(file_path)
            raise forms.ValidationError(str(e))

        return file