import os
from moviepy.editor import VideoFileClip

from django.db import models
from django.utils.translation import gettext_lazy as _

def convert_to_mp3(file_path):
    """
    Convert MP4 to MP3 or verify MP3 file.
    Raises error for unsupported file types.
    """
    # Get file extension
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # If MP4, convert to MP3
    if extension == '.mp4':
        try:
            # Get the directory path and filename
            directory = os.path.dirname(file_path)
            filename = os.path.basename(file_path)

            # Replace 'video' with 'audio' in the directory path
            audio_directory = directory.replace('video', 'audio')

            # Create audio directory if it doesn't exist
            if not os.path.exists(audio_directory):
                os.makedirs(audio_directory)

            # Create output path with mp3 extension
            output_path = os.path.join(audio_directory, filename.rsplit('.', 1)[0] + '.mp3')

            # Convert video to audio
            video = VideoFileClip(file_path)
            video.audio.write_audiofile(output_path)
            video.close()

            return output_path

        except Exception as e:
            raise Exception(f"Error converting MP4 to MP3: {str(e)}")

    # If MP3, return the path as is
    elif extension == '.mp3':
        return file_path

    # For any other extension, raise error
    else:
        raise ValueError(f"Unsupported file format: {extension}. Only MP4 and MP3 files are supported.")


class LanguageChoices(models.TextChoices):
    English = 'en', _('English')
    German = 'de', _('German')
    Spanish = 'es', _('Spanish')
    French = 'fr', _('French')
    Arabic = 'ar', _('Arabic')

class TrnsChoices(models.TextChoices):
    PENDING = 'pending', _('Pending')
    DONE = 'done', _('Done')
    FAILED = 'failed', _('Failed')

class ModelSizeChoices(models.TextChoices):
    TINY = 'tiny', 'Tiny'
    BASE = 'base', 'Base'
    SMALL = 'small', 'Small'
    MEDIUM = 'medium', 'Medium'
    LARGE_V1 = 'large-v1', 'Large v1'
    LARGE_V2 = 'large-v2', 'Large v2'
    LARGE_V3 = 'large-v3', 'Large v3'
    LARGE = 'large', 'Large'
    DISTIL_LARGE_V2 = 'distil-large-v2', 'Distil Large v2'
    DISTIL_LARGE_V3 = 'distil-large-v3', 'Distil Large v3'