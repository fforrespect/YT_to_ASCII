import os
import time
import pickle

from Draw import AsciiArt
from Vars import Global

all_frames = os.listdir(Global.frames_fp)
all_frame_nums = [int(x[5:-4]) for x in all_frames if x[-4:] == ".jpg"]


def create_strings():
    print("Creating frame strings...")

    frame_strings = []

    for frame_number in range(max(all_frame_nums)):
        # start = time.time()
        image_file_path = f"{Global.frames_fp}frame{frame_number}.jpg"

        frame_strings.append(AsciiArt.image_to_string(image_file_path))

    os.remove(Global.strings_fp)

    strings_file = open(Global.strings_fp, 'ab')
    pickle.dump(frame_strings, strings_file)
    strings_file.close()

    print("All frame strings created and pickled")
    print()


def draw():
    # frame_strings = []
    #
    # for frame_number in range(max(all_frame_nums)):
    #     # start = time.time()
    #     image_file_path = f"{Global.frames_fp}frame{frame_number}.jpg"
    #
    #     frame_strings.append(AsciiArt.image_to_string(image_file_path))
    #     # print(("\n"*200) + string)
    #
    #     # time.sleep(max(1/Global.fps - (time.time() - start), 0))

    strings_file = open(Global.strings_fp, 'rb')
    frame_strings = pickle.load(strings_file)
    strings_file.close()

    for string in frame_strings:
        start = time.time()
        print("\n"*200)
        print(string)
        time.sleep(max(1/Global.fps - (time.time() - start), 0))
