from Process import YTVid, VideoFrames

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_fp = "../resources/videos/"
video_name = "nggyu.mp4"

frames_fp = "../resources/frames/"

YTVid.download(video_url, video_fp, video_name)
VideoFrames.download(video_fp + video_name, frames_fp)
