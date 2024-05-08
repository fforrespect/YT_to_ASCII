# -- Rick Astley --
# VIDEO_URL: str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# -- F1 --
# VIDEO_URL: str = "https://www.youtube.com/watch?v=VTAPL-xz7HY"

# -- 30 secs --
# VIDEO_URL: str = "https://www.youtube.com/watch?v=0yZcDeVsj_Y"

# -- Nyan Cat 5 secs --
VIDEO_URL: str = "https://www.youtube.com/watch?v=9HQzRxmr87s"


VIDEO_FP: str = "../resources/videos/"
VIDEO_NAME: str = "video_to_process.mp4"

AUDIO_FP: str = "../resources/audio/yt_video_audio.mp3"

FRAMES_FP: str = "../resources/frames/"
FRAME_EXT: str = ".jpg"

STRINGS_FP: str = "../resources/strings/frame_strings.txt"

DELIMITER: str = "ARBITRARY_DELIMITER"

LOADING_BAR_FILL: str = '█'
LOADING_BAR_SUFFIX: str = "%(index)d/%(max)d (%(percent).1f%%) - %(elapsed)ds elapsed (eta %(eta)ds)"


FPS: int
SKIP: int = 2
NEW_FPS: float  # will be equal to fps/skip

DISPLAY_WIDTH: int = 300
