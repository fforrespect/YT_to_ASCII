from moviepy.editor import VideoFileClip
from pygame import mixer

from Meta import GlobalVars


def create_file():
    print("Creating audio file...")

    video = VideoFileClip(GlobalVars.video_fp + GlobalVars.video_name)
    video.audio.write_audiofile(GlobalVars.audio_fp)

    print("Audio file created")
    print()


def play():
    mixer.init()
    mixer.music.load(GlobalVars.audio_fp)
    mixer.music.play()
