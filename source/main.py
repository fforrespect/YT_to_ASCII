from threading import Thread

from Meta.GlobalVars import *
from Output import AllFrames
from Process import YTVid, VideoFrames, ResizeAllFrames, Audio

# Pre-processing
YTVid.download(video_url, video_fp, video_name)
VideoFrames.download(video_fp + video_name, frames_fp)
ResizeAllFrames.process()
AllFrames.create_strings()
Audio.create_file()

input("Press enter to play video... ")

# Playing video
audio_thread: Thread = Thread(target=Audio.play)
video_thread: Thread = Thread(target=AllFrames.draw)

audio_thread.start()
video_thread.start()

# End
audio_thread.join()
video_thread.join()
