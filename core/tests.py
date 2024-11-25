from moviepy.editor import VideoFileClip
import os

from faster_whisper import WhisperModel
# (tiny, tiny.en, base, base.en,
#             small, small.en, distil-small.en, medium, medium.en, distil-medium.en, large-v1,
#             large-v2, large-v3, large, distil-large-v2 or distil-large-v3)



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
            # Create output path by changing extension to mp3
            output_path = file_path.rsplit('.', 1)[0] + '.mp3'

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



audio_path = convert_to_mp3("test.mp4")

model_size = "base"
model = WhisperModel(model_size, device="cpu")
segments, info = model.transcribe(audio_path, beam_size=5, language="de", condition_on_previous_text=False)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))