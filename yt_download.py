from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def yt_download(link, save_path):
    try:
        yt = YouTube(link)
    except VideoUnavailable:
        print("Video unavailable")
    else:
        print(f"Downloading {yt.title}")
        video = yt.streams.get_by_itag(22)
        video.download(save_path)
