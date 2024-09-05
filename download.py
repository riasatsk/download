import os
import yt_dlp

def is_valid_url(url):
    # Custom logger that ignores all messages
    class MyLogger(object):
        def debug(self, msg):
            pass

        def info(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            pass

    ydl_opts = {
        'quiet': True,  # Suppress output
        'no_warnings': True,  # Suppress warnings
        'logger': MyLogger(),  # Use custom logger to suppress error messages
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
            return True
    except Exception:
        print(f"\033[31mThe provided URL '{url}' is not valid.\033[0m")
        return False
    

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join("D:/Music/", '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: The video URL '{url}' is not working or cannot be downloaded.")


def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio streams and merge them.
        'outtmpl': os.path.join("D:/Video/", '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  # Merge into mp4 container.
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: The video URL '{url}' is not working or cannot be downloaded.")


def download(url):
    print("What would you like to download?")
    print("1: Audio")
    print("2: Video")
    select = input("Enter 1 or 2: ")

    if select == '1':
        download_audio(url)
    elif select == '2':
        download_video(url)
    else:
        print("Invalid selection. Please press 1 or 2.")
        download(url)


video_url = input("Please enter a URL: ")

# Validate the user-provided URL if it wasn't valid initially
while not is_valid_url(video_url):
    video_url = input("Please enter a valid URL: ")

download(video_url)