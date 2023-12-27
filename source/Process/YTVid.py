import pytube


def download(url, filepath, file_name=None):
    yt_object = pytube.YouTube(url)
    yt_object = yt_object.streams.get_highest_resolution()
    yt_object.download(filepath, filename=file_name)

    print("Download completed successfully")
