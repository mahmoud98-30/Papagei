from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', upload_media_file, name='upload_media_file'),
    path('list_files/', list_files, name='list_files'),
    path('delete/<int:pk>/', delete_file, name='delete_file'),
    path('support/', support, name='support'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)