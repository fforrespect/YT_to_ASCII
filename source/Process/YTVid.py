from pytube import YouTube


def download(url, filepath, file_name=None):
    print("Downloading video...")

    yt_object = YouTube(url)
    yt_object = yt_object.streams.get_highest_resolution()
    yt_object.download(filepath, filename=file_name)

    print("Video download completed")
    print("Title:", yt_object.title)
    print()
