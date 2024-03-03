from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame.mixer import init, music

from Meta import Constants as c


def create_file() -> None:
    print("Creating audio file...")

    video: VideoFileClip = VideoFileClip(c.video_fp + c.video_name)
    video.audio.write_audiofile(c.audio_fp)

    print("Audio file created")
    print()


def play() -> None:
    init()
    music.load(c.audio_fp)
    music.play()
