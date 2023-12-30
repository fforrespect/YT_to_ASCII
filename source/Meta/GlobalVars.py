# Rick Astley
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# F1
# video_url = "https://www.youtube.com/watch?v=VTAPL-xz7HY"
# 30 secs
# video_url = "https://www.youtube.com/watch?v=0yZcDeVsj_Y"

video_fp = "../resources/videos/"
video_name = "video_to_display.mp4"

audio_fp = "../resources/audio/audio_to_play.mp3"

frames_fp = "../resources/frames/"
frame_ext = ".jpg"

strings_fp = "../resources/strings/frame_strings.txt"

delimiter = "ARBITRARY_DELIMITER"


fps = None
skip = 4

new_fps = fps/skip if fps is not None else None

width = 300
