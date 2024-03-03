from os import listdir
from PIL.Image import open, Image

from Meta import GlobalVars


def process() -> None:
    print("Resizing frames...")

    all_frames: list[str] = listdir(GlobalVars.frames_fp)
    all_frames = list(filter(lambda x: x[-4:] == GlobalVars.frame_ext, all_frames))

    frame: Image = open(GlobalVars.frames_fp + all_frames[0])
    size: tuple[int, int] = frame.size

    new_size_x: int = GlobalVars.width
    new_size_y: int = round(size[1]/(size[0]/new_size_x))

    for frame_filename in all_frames:
        image_file_path: str = GlobalVars.frames_fp + frame_filename

        frame = open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        frame.save(image_file_path)

    print("All frames resized")
    print("Video resolution:", (new_size_x, new_size_y))
    print()
