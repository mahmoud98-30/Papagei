from django.db import models

from core.utils import LanguageChoices,TrnsChoices

class Transcribe(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=LanguageChoices.choices)
    audio = models.FileField(upload_to='uploads/audio/')
    output_file = models.FileField(upload_to='uploads/output_file/', blank=True, null=True)
    status = models.CharField(max_length=10, default='pending', choices=TrnsChoices.choices)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language} - {self.audio.name}"
