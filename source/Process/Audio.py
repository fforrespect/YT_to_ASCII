from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame.mixer import init, music

from Meta import Constants as c


def create_file() -> None:
    print("Creating audio file...")

    video: VideoFileClip = VideoFileClip(c.VIDEO_FP + c.VIDEO_NAME)
    video.audio.write_audiofile(c.AUDIO_FP)

    print("Audio file created")
    print()


def play() -> None:
    init()
    music.load(c.AUDIO_FP)
    music.play()
