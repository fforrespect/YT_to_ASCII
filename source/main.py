import threading

from Draw import AllFrames
from Vars.Global import *
from Process import YTVid, VideoFrames, ResizeAllFrames, Audio

YTVid.download(video_url, video_fp, video_name)
VideoFrames.download(video_fp + video_name, frames_fp)
ResizeAllFrames.process()
frame_strings = AllFrames.create_strings()
Audio.create_file()

audio_thread = threading.Thread(target=Audio.play)
video_thread = threading.Thread(target=AllFrames.draw)

audio_thread.start()
video_thread.start()

audio_thread.join()
video_thread.join()
