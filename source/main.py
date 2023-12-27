from Draw import AllFrames
from Vars.Global import *
from Process import YTVid, VideoFrames, ResizeAllFrames

YTVid.download(video_url, video_fp, video_name)
VideoFrames.download(video_fp + video_name, frames_fp)
ResizeAllFrames.process()
frame_strings = AllFrames.create_strings()

AllFrames.draw()
