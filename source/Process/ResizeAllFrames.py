import os
from PIL import Image

from Meta import GlobalVars

all_frames = os.listdir(GlobalVars.frames_fp)
all_frames = [x for x in all_frames if x[-4:] == GlobalVars.frame_ext]


def process():
    print("Resizing frames...")

    frame = Image.open(GlobalVars.frames_fp + all_frames[0])
    size = frame.size

    new_size_x = GlobalVars.width
    new_size_y = round(size[1]/(size[0]/new_size_x))

    for frame_filename in all_frames:
        image_file_path = GlobalVars.frames_fp + frame_filename

        frame = Image.open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        frame.save(image_file_path)

    print("All frames resized")
    print("Video resolution:", (new_size_x, new_size_y))
    print()
