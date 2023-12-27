import os

from Draw import AsciiArt
from File import Path

all_frames = os.listdir(Path.frames_fp)


def draw():
    for frame_filename in [x for x in all_frames if x[-4:] == ".jpg"]:
        image_file_path = Path.frames_fp + frame_filename

        string = AsciiArt.image_to_string(image_file_path, in_place=False)
        print(("\n"*100) + string)
