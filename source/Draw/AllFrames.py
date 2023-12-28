import os
import time
import pickle

from Draw import AsciiArt
from Meta import GlobalVars

all_frames = os.listdir(GlobalVars.frames_fp)
all_frame_nums = [int(x[5:-4]) for x in all_frames if x[-4:] == GlobalVars.frame_ext]


def create_strings():
    print("Creating frame strings...")

    frame_strings = []

    for frame_number in range(max(all_frame_nums)):
        # start = time.time()
        image_file_path = f"{GlobalVars.frames_fp}frame{frame_number}{GlobalVars.frame_ext}"

        frame_strings.append(AsciiArt.image_to_string(image_file_path))

    os.remove(GlobalVars.strings_fp)

    strings_file = open(GlobalVars.strings_fp, 'ab')
    pickle.dump(frame_strings, strings_file)
    strings_file.close()

    print("All frame strings created and pickled")
    print()


def draw():
    with open(GlobalVars.strings_fp, 'rb') as strings_file:
        frame_strings = pickle.load(strings_file)

    frame_time = 1 / GlobalVars.fps
    next_frame_time = time.time() + frame_time

    for string in frame_strings:
        _clear_screen()
        print(string)

        sleep_time = next_frame_time - time.time()
        time.sleep(max(sleep_time, 0))
        next_frame_time += frame_time


def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
