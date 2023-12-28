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
    strings_file = open(GlobalVars.strings_fp, 'rb')
    frame_strings = pickle.load(strings_file)
    strings_file.close()

    for string in frame_strings:
        start = time.time()
        print("\n"*200)
        print(string)
        time.sleep(max(1/GlobalVars.fps - (time.time() - start), 0))
