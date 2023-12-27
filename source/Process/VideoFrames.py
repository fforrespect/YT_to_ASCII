import os
import glob
import cv2

from Vars import Global


def download(from_path, to_path):
    files = glob.glob(f"{to_path}*")
    for f in files:
        os.remove(f)

    # file = [x for x in os.listdir(from_path) if x[-1] == "4"][0]
    file = from_path

    vid_cap = cv2.VideoCapture(file)
    Global.fps = vid_cap.get(cv2.CAP_PROP_FPS)/Global.skip
    print(Global.fps)

    success, image = vid_cap.read()

    frame = 0
    while success:
        if frame % Global.skip == 0:
            cv2.imwrite(f"{to_path}frame{int(frame/Global.skip)}.jpg", image)
            success, image = vid_cap.read()
        frame += 1

    print("All frames created")
