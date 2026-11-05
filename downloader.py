
import yt_dlp
import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent
ffmpeg_path = base_dir / 'ffmpeg' / 'bin' / 'ffmpeg.exe'


def download(url, download_path):

    # Default to the user's actual Windows Downloads folder
    if not download_path:
        download_path = str(Path.home() / 'Downloads')

    # Expand environment variables and ~
    download_path = os.path.expandvars(os.path.expanduser(download_path))

    # Convert relative paths to paths relative to the project directory
    if not os.path.isabs(download_path):
        download_path = str(base_dir / download_path)

    os.makedirs(download_path, exist_ok=True)

    if not ffmpeg_path.is_file():
        raise FileNotFoundError(
            f"FFmpeg was not found at:\n{ffmpeg_path}"
        )

    options = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bv*+ba/b',
        'ffmpeg_location': str(ffmpeg_path),
        'noplaylist': True,
        'verbose': True,
        'paths': {
            'home': download_path
        }
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
