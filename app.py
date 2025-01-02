import os
from yt_dlp import YoutubeDL


def download_youtube_audio_as_mp3(youtube_url, output_folder="downloads"):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Set download options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'ffmpeg_location': r"C:\Users\kotel\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe",
        }

        # Download and convert audio
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_link = input("Enter the YouTube video link: ")
    download_youtube_audio_as_mp3(youtube_link)
