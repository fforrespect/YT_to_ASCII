from os import listdir, system, remove
from sys import stdout
from time import time, sleep
from progress.bar import ChargingBar

from Process.AsciiArt import image_to_string
from Meta import Constants as c, GlobalVars as gv, File


def create_strings() -> None:
    all_frames: list[str] = listdir(c.FRAMES_FP)
    all_frame_nums: list[int] = [int(x[5:-4]) for x in all_frames if x[-4:] == c.FRAME_EXT]

    bar = ChargingBar(
        "Creating frame strings",
        max=len(all_frame_nums),
        fill=c.LOADING_BAR_FILL,
        suffix=c.LOADING_BAR_SUFFIX
    )

    frame_strings: list[str] = []

    for frame_number in range(max(all_frame_nums)+1):
        image_file_path: str = f"{c.FRAMES_FP}frame{frame_number}{c.FRAME_EXT}"

        frame_strings.append(image_to_string(image_file_path))
        frame_strings.append(c.DELIMITER)

        if gv.destructive:
            remove(image_file_path)

        bar.next()
        
    File.delete_if_extant(c.STRINGS_FP)
    with open(c.STRINGS_FP, "w") as strings_file:
        strings_file.writelines(frame_strings)

    bar.finish()

    print("All frame strings created and stored\n")


def draw() -> None:
    with open(c.STRINGS_FP, "r") as strings_file:
        frame_strings: list[str] = "".join(strings_file.readlines()).split(c.DELIMITER)
    
    if gv.destructive:
        remove(c.STRINGS_FP)

    frame_time: float = 1 / c.NEW_FPS
    next_frame_time: float = time() + frame_time

    for string in frame_strings:
        system("clear")  # _clear_screen()
        # print(string, flush=True)
        stdout.write(string)
        stdout.flush()

        sleep_time: float = next_frame_time - time()
        sleep(max(sleep_time, 0))
        next_frame_time += frame_time


# def _clear_screen() -> None:
#     # 'nt' being Windows, 'clear' works for all other OSs
#     system('cls' if name == 'nt' else 'clear')
