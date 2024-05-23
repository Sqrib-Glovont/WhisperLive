import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
from whisper_live.client import TranscriptionClient

def download_youtube_video_as_wav(url, output_path):
    # Download the video from YouTube using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, 'temp_audio.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        wav_file = ydl.prepare_filename(info_dict).replace('.webm', '.wav').replace('.m4a', '.wav')

    return wav_file

# URL of the YouTube video
youtube_url = "https://www.youtube.com/watch?v=cx4LaLSdCa4&ab_channel=BloombergTelevision"
output_directory = "tests"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Download and convert the video to WAV format
wav_file_path = download_youtube_video_as_wav(youtube_url, output_directory)

# Run the transcription client on the downloaded WAV file
client = TranscriptionClient(
    "localhost",
    9090,
    lang="en",
    translate=False,
    model="small",
    use_vad=False,
)

client(wav_file_path)

