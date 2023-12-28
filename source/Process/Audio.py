from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub import playback

from Meta import GlobalVars


def create_file():
    print("Creating audio file...")

    video = VideoFileClip(GlobalVars.video_fp + GlobalVars.video_name)
    video.audio.write_audiofile(GlobalVars.audio_fp)

    print("Audio file created")
    print()


# def create_clips():
#     print("Creating audio clips...")


def play():
    audio = AudioSegment.from_mp3(GlobalVars.audio_fp)
    playback.play(audio)
