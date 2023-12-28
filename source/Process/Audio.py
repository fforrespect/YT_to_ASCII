from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub import playback

from Vars import Global


def create_file():
    print("Creating audio file...")

    video = VideoFileClip(Global.video_fp + Global.video_name)
    video.audio.write_audiofile(Global.audio_fp)

    print("Audio file created")
    print()


# def create_clips():
#     print("Creating audio clips...")


def play():
    audio = AudioSegment.from_mp3(Global.audio_fp)
    playback.play(audio)
