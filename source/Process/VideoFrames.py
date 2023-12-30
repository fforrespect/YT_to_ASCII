from os import listdir, remove
from glob import glob
from cv2 import VideoCapture, imwrite, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT

from Meta import GlobalVars


def download(from_path, to_path):
    print("Downloading frames...")

    files = glob(f"{to_path}*")
    for f in files:
        remove(f)

    file = from_path

    vid_cap = VideoCapture(file)
    GlobalVars.fps = vid_cap.get(CAP_PROP_FPS)
    GlobalVars.new_fps = GlobalVars.fps / GlobalVars.skip
    total_frames = int(vid_cap.get(CAP_PROP_FRAME_COUNT))

    success, image = vid_cap.read()

    frame = 0
    while success:
        if frame % GlobalVars.skip == 0:
            cv2.imwrite(f"{to_path}frame{int(frame/GlobalVars.skip)}{GlobalVars.frame_ext}", image)
            success, image = vid_cap.read()
        frame += 1

    print("All frames created")
    print("FPS:", GlobalVars.fps)
    print("Adjusted FPS:", GlobalVars.new_fps)
    print("Total frames:", len(listdir(GlobalVars.frames_fp))-1)
    print()
