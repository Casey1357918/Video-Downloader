import yt_dlp
import ffmpeg
import ffmpeg_downloader as ffmpeg
import os
from datetime import datetime
from pathlib import Path




base_dir = Path(__file__).resolve().parent
ffmpeg_path=str(base_dir)+"\\ffmpeg\\bin\\ffmpeg.exe"

def download(url , download_path):
    
    if download_path == "":
        download_path='C:\\Users\\'+os.getenv('username')+'\\Downloads'
    
    
    output_name='%(title)s.%(ext)s'
    if '#' in output_name:
        output_name=output_name[0:output_name.index('#')]



    options={ 'outtmpl': output_name, 'format': 'bv*+ba/b', 'ffmpeg_location': ffmpeg_path, 'wait-for-video': 5, 'wait-for-video-retries': 100000000000, 'paths': {'home': download_path}}
    
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

