from os import listdir, remove
from glob import glob
from cv2 import VideoCapture, imwrite, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT, Mat
from progress.bar import ChargingBar

from Meta import Constants as c


def download(from_path: str, to_path: str) -> None:
    files: list[str] = glob(f"{to_path}*")
    
    for f in files:
        remove(f)

    file: str = from_path

    vid_cap: VideoCapture = VideoCapture(file)
    c.FPS = vid_cap.get(CAP_PROP_FPS)
    c.NEW_FPS = c.FPS / c.SKIP
    total_frames: int = int(vid_cap.get(CAP_PROP_FRAME_COUNT))

    bar = ChargingBar(
        "Downloading Frames",
        max=total_frames//c.SKIP,
        fill=c.LOADING_BAR_FILL,
        suffix=c.LOADING_BAR_SUFFIX
    )

    for frame_number in range(total_frames):
        success: bool
        image: Mat
        success, image = vid_cap.read()

        if frame_number % c.SKIP != 0:
            continue

        if not success:
            break

        file_path: str = f"{to_path}frame{frame_number//c.SKIP}{c.FRAME_EXT}"

        imwrite(file_path, image)
        bar.next()

    # Release the video capture object
    vid_cap.release()

    bar.finish()

    print(len(listdir(c.FRAMES_FP)) - 1, "frames created")
    if c.SKIP != 1:
        print("Original FPS:", round(c.FPS, 2))
        print("Adjusted FPS:", round(c.NEW_FPS, 2))
    else:
        print("FPS:", round(c.FPS, 2))
    print()
