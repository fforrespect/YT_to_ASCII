import os
from PIL import Image

from Vars import Global

all_frames = os.listdir(Global.frames_fp)
all_frames = [x for x in all_frames if x[-4:] == ".jpg"]


def process():
    frame = Image.open(Global.frames_fp + all_frames[0])
    size = frame.size

    new_size_x = Global.width
    new_size_y = round(size[1]/(size[0]/new_size_x))

    for frame_filename in all_frames:
        image_file_path = Global.frames_fp + frame_filename

        frame = Image.open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        frame.save(image_file_path)

    print("All frames resized")
