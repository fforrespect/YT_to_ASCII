from moviepy.editor import VideoFileClip
from pygame.mixer import init, music

from Meta import GlobalVars


def create_file():
    print("Creating audio file...")

    video = VideoFileClip(GlobalVars.video_fp + GlobalVars.video_name)
    video.audio.write_audiofile(GlobalVars.audio_fp)

    print("Audio file created")
    print()


def play():
    init()
    music.load(GlobalVars.audio_fp)
    music.play()
