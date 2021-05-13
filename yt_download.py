from pytube import YouTube
from pytube.exceptions import *


def yt_download(link, save_path):
    try:
        yt = YouTube(link)
    except PytubeError:
        print("Video unavailable")
    else:
        print(f"Downloading {yt.title}")
        video = yt.streams.filter(progressive=True).get_highest_resolution()
        video.download(save_path)
