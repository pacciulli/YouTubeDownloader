from pytube import YouTube
from pytube.exceptions import *
from pytube.cli import on_progress
from moviepy.editor import *


def yt_download(link, save_path, resolution):

    if resolution == "SD":
        try:
            yt = YouTube(link)
            yt.register_on_progress_callback(on_progress)
            print(f"Downloading {yt.title}")
            video = yt.streams.filter(progressive=True).get_highest_resolution()
            video.download(save_path)
        except PytubeError:
            print("Video unavailable")

    else:
        video_path = f"{save_path}\\video"
        audio_path = f"{save_path}\\audio"

        try:
            yt = YouTube(link)
            yt.register_on_progress_callback(on_progress)
            print(f"Downloading {yt.title}")
            video = (
                yt.streams.filter(adaptive=True, only_video=True, subtype="mp4")
                .order_by("resolution")
                .last()
            )
            video_name = video.download(video_path)
            audio = (
                yt.streams.filter(adaptive=True, only_audio=True, subtype="mp4")
                .order_by("abr")
                .last()
            )
            audio_name = audio.download(audio_path)

            video_clip = VideoFileClip(video_name)
            audio_clip = AudioFileClip(audio_name)

            video_clip.audio = CompositeAudioClip([audio_clip])
            save_name = f"{save_path}\\{yt.title}.mp4"
            video_clip.write_videofile(save_name)

        except PytubeError:
            print("Video unavailable")
