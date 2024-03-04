from threading import Thread

from Meta.Constants import *
from Output import AllFrames
from Process import YTVid, VideoFrames, ResizeAllFrames, Audio

# Pre-processing
YTVid.download(VIDEO_URL, VIDEO_FP, VIDEO_NAME)
VideoFrames.download(VIDEO_FP + VIDEO_NAME, FRAMES_FP)
ResizeAllFrames.process()
AllFrames.create_strings()
Audio.create_file()

input("Press enter to play video... ")

# Play video
audio_thread: Thread = Thread(target=Audio.play)
video_thread: Thread = Thread(target=AllFrames.draw)

audio_thread.start()
video_thread.start()

# End
audio_thread.join()
video_thread.join()
