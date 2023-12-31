from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame.mixer import init, music

from Meta import GlobalVars


def create_file() -> None:
    print("Creating audio file...")

    video: VideoFileClip = VideoFileClip(GlobalVars.video_fp + GlobalVars.video_name)
    video.audio.write_audiofile(GlobalVars.audio_fp)

    print("Audio file created")
    print()


def play() -> None:
    init()
    music.load(GlobalVars.audio_fp)
    music.play()
