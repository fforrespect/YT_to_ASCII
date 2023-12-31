from os import listdir, remove
from glob import glob

from cv2 import VideoCapture, imwrite, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT, Mat

from Meta import GlobalVars


def download(from_path: str, to_path: str) -> None:
    print("Downloading frames...")

    files: list[str] = glob(f"{to_path}*")
    for f in files:
        remove(f)

    file: str = from_path

    vid_cap: VideoCapture = VideoCapture(file)
    GlobalVars.fps = vid_cap.get(CAP_PROP_FPS)
    GlobalVars.new_fps = GlobalVars.fps / GlobalVars.skip
    total_frames: int = int(vid_cap.get(CAP_PROP_FRAME_COUNT))

    for frame_number in range(total_frames):
        success: bool
        image: Mat
        success, image = vid_cap.read()

        if frame_number % GlobalVars.skip == 0:
            continue

        if not success:
            break

        imwrite(f"{to_path}frame{int(frame_number/GlobalVars.skip)}{GlobalVars.frame_ext}", image)

    # Release the video capture object
    vid_cap.release()

    print("All frames created")
    print("FPS:", GlobalVars.fps)
    print("Adjusted FPS:", GlobalVars.new_fps)
    print("Total frames:", len(listdir(GlobalVars.frames_fp))-1)
    print()
