import os
import glob
import cv2

from Meta import GlobalVars


def download(from_path, to_path):
    print("Downloading frames...")

    files = glob.glob(f"{to_path}*")
    for f in files:
        os.remove(f)

    # file = [x for x in os.listdir(from_path) if x[-1] == "4"][0]
    file = from_path

    vid_cap = cv2.VideoCapture(file)
    GlobalVars.fps = vid_cap.get(cv2.CAP_PROP_FPS)/GlobalVars.skip

    success, image = vid_cap.read()

    frame = 0
    while success:
        if frame % GlobalVars.skip == 0:
            cv2.imwrite(f"{to_path}frame{int(frame/GlobalVars.skip)}{GlobalVars.frame_ext}", image)
            success, image = vid_cap.read()
        frame += 1

    print("All frames created")
    print("FPS:", GlobalVars.fps)
    print("Total frames:", len(os.listdir(GlobalVars.frames_fp))-1)
    print()
