from threading import Thread

from Output.AllFrames import *
from Meta.GlobalVars import *
from Process import YTVid, VideoFrames, ResizeAllFrames, Audio

YTVid.download(video_url, video_fp, video_name)
VideoFrames.download(video_fp + video_name, frames_fp)
ResizeAllFrames.process()
frame_strings = create_strings()
Audio.create_file()

audio_thread = Thread(target=Audio.play)
video_thread = Thread(target=draw)

audio_thread.start()
video_thread.start()

audio_thread.join()
video_thread.join()
