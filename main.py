import sys
import os.path

from yt_download import yt_download
from createThreads import create_threads


# Get path function
def get_path(file_name):
    path = input(f"Insert {file_name} path: ")
    return path


# Download videos function
def download_videos():
    file_path = get_path("Videos Link file")

    # Check if file with links is valid
    if os.path.isfile(file_path):
        print("\n** Links file is valid **\n")
    else:
        print(f"\n** File {file_path} does not exist. Please check and try again! **\n")
        sys.exit()

    save_path = get_path("Save")

    # This section open links file, read it and remove \n chars
    file = open(file_path, "r")
    file.seek(0)
    video_list = file.readlines()

    for x in range(0, len(video_list)):
        video_list[x] = video_list[x].rstrip("\n")

    file.close()

    hd = input(f"Download in HD (Y/N)?").upper()
    if hd == "Y":
        resolution = "HD"
    else:
        resolution = "SD"

    # Create and execute threads
    create_threads(video_list, save_path, yt_download, resolution)


if __name__ == "__main__":
    download_videos()
