from os import remove
from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame import mixer
from pygame.mixer import music

from Meta import Constants as c


def create_file() -> None:
    print("Creating audio file...")

    video: VideoFileClip = VideoFileClip(c.VIDEO_FP + c.VIDEO_NAME)
    video.audio.write_audiofile(c.AUDIO_FP)
    remove(c.VIDEO_FP + c.VIDEO_NAME)

    print("Audio file created")
    print()


def play() -> None:
    mixer.init()
    music.load(c.AUDIO_FP)
    music.play()

    remove(c.AUDIO_FP)
