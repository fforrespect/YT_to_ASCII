import os
from PIL import Image

from File import Path

all_frames = os.listdir(Path.frames_fp)


def process():
    frame = Image.open(Path.frames_fp + all_frames[0])
    size = frame.size

    width = 700

    new_size_x = width
    new_size_y = round(size[1]/(size[0]/width))

    for frame_filename in [x for x in all_frames if x[-4:] == ".jpg"]:
        image_file_path = Path.frames_fp + frame_filename

        frame = Image.open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        frame.save(image_file_path)

    print("All frames resized")
