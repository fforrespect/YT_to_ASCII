from os import listdir, system, name, remove
from time import time, sleep

from Process.AsciiArt import image_to_string
from Meta import GlobalVars

all_frames = listdir(GlobalVars.frames_fp)
all_frame_nums = [int(x[5:-4]) for x in all_frames if x[-4:] == GlobalVars.frame_ext]


def create_strings():
    print("Creating frame strings...")

    frame_strings = []

    for frame_number in range(max(all_frame_nums)):
        # start = time.time()
        image_file_path = f"{GlobalVars.frames_fp}frame{frame_number}{GlobalVars.frame_ext}"

        frame_strings.append(image_to_string(image_file_path))
        frame_strings.append(GlobalVars.delimiter)

    remove(GlobalVars.strings_fp)

    with open(GlobalVars.strings_fp, "w") as strings_file:
        strings_file.writelines(frame_strings)

    print("All frame strings created and stored")
    print()


def draw():
    with open(GlobalVars.strings_fp, "r") as strings_file:
        frame_strings = "".join(strings_file.readlines()).split(GlobalVars.delimiter)

    frame_time = 1 / GlobalVars.new_fps
    next_frame_time = time() + frame_time

    for string in frame_strings:
        _clear_screen()
        print(string)

        sleep_time = next_frame_time - time()
        sleep(max(sleep_time, 0))
        next_frame_time += frame_time


def _clear_screen():
    system('cls' if name == 'nt' else 'clear')
