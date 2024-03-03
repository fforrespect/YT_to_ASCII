from os import listdir, system, remove
from time import time, sleep
from progress.bar import Bar

from Process.AsciiArt import image_to_string
from Meta import GlobalVars


def create_strings() -> None:
    all_frames: list[str] = listdir(GlobalVars.frames_fp)
    all_frame_nums: list[int] = [int(x[5:-4]) for x in all_frames if x[-4:] == GlobalVars.frame_ext]

    bar = Bar(
        'Creating frame strings',
        max=len(all_frames),
        suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds'
    )

    frame_strings: list[str] = []

    for frame_number in range(max(all_frame_nums)):
        image_file_path: str = f"{GlobalVars.frames_fp}frame{frame_number}{GlobalVars.frame_ext}"

        frame_strings.append(image_to_string(image_file_path))
        frame_strings.append(GlobalVars.delimiter)

        bar.next()

    remove(GlobalVars.strings_fp)

    with open(GlobalVars.strings_fp, "w") as strings_file:
        strings_file.writelines(frame_strings)

    bar.finish()

    print("All frame strings created and stored\n")


def draw() -> None:
    with open(GlobalVars.strings_fp, "r") as strings_file:
        frame_strings: list[str] = "".join(strings_file.readlines()).split(GlobalVars.delimiter)

    frame_time: float = 1 / GlobalVars.new_fps
    next_frame_time: float = time() + frame_time

    for string in frame_strings:
        system("clear")  # _clear_screen()
        print(string)

        sleep_time: float = next_frame_time - time()
        sleep(max(sleep_time, 0))
        next_frame_time += frame_time


# def _clear_screen() -> None:
#     system('cls' if name == 'nt' else 'clear')
