from threading import Thread
import sys

from Output import AllFrames
from Process import YTVid, VideoFrames, ResizeAllFrames, Audio
from Meta.Constants import *
from Meta import File

File.check_is_destructive(sys.argv)

# Pre-processing
File.delete_all()
YTVid.download(VIDEO_URL, VIDEO_FP, VIDEO_NAME)
VideoFrames.download(VIDEO_FP + VIDEO_NAME, FRAMES_FP)
ResizeAllFrames.process()
AllFrames.create_strings()
# gv.compressed_frames = Compression.compress_colours()
Audio.create_file()

input("Press enter to play video... ")

# Play video
audio_thread: Thread = Thread(target=Audio.play)
video_thread: Thread = Thread(target=AllFrames.draw)
# video_thread: Thread = Thread(target=Compression.decompress_and_draw)

audio_thread.start()
video_thread.start()

# End
audio_thread.join()
video_thread.join()
