from pytube import YouTube


def download(url: str, filepath: str, file_name: str | None = None) -> None:
    print("\nDownloading video...")

    yt_object = YouTube(url)
    yt_object = yt_object.streams.get_highest_resolution()
    yt_object.download(filepath, filename=file_name)

    print("Video download completed")
    print("Title:", yt_object.title)
    print()
