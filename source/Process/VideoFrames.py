from os import listdir, remove
from glob import glob
from cv2 import VideoCapture, imwrite, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT, Mat
from progress.bar import Bar

from Meta import GlobalVars


def download(from_path: str, to_path: str) -> None:
    files: list[str] = glob(f"{to_path}*")
    for f in files:
        remove(f)

    file: str = from_path

    vid_cap: VideoCapture = VideoCapture(file)
    GlobalVars.fps = vid_cap.get(CAP_PROP_FPS)
    GlobalVars.new_fps = GlobalVars.fps / GlobalVars.skip
    total_frames: int = int(vid_cap.get(CAP_PROP_FRAME_COUNT))

    bar = Bar(
        "Downloading Frames",
        max=total_frames//GlobalVars.skip,
        fill='█',
        suffix="%(index)d/%(max)d - %(percent).1f%% - %(eta)ds"
    )

    for frame_number in range(total_frames):
        success: bool
        image: Mat
        success, image = vid_cap.read()

        if frame_number % GlobalVars.skip == 0:
            continue

        if not success:
            break

        file_path: str = f"{to_path}frame{frame_number//GlobalVars.skip}{GlobalVars.frame_ext}"

        try: remove(file_path)
        except FileNotFoundError: pass
        imwrite(file_path, image)
        bar.next()

    # Release the video capture object
    vid_cap.release()

    bar.finish()

    print(len(listdir(GlobalVars.frames_fp))-1, "frames created")
    print("Original FPS:", GlobalVars.fps)
    print("Adjusted FPS:", GlobalVars.new_fps)
    print()
