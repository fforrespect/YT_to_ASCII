from os import listdir, remove
from PIL.Image import open, Image
from progress.bar import ChargingBar

from Meta import Constants as c, File


def process() -> None:
    all_frames: list[str] = listdir(c.FRAMES_FP)
    all_frames = list(filter(lambda x: x[-4:] == c.FRAME_EXT, all_frames))

    bar = ChargingBar(
        "Resizing Frames",
        max=len(all_frames),
        fill=c.LOADING_BAR_FILL,
        suffix=c.LOADING_BAR_SUFFIX
    )

    frame: Image = open(c.FRAMES_FP + all_frames[0])
    size: tuple[int, int] = frame.size

    new_size_x: int = c.DISPLAY_WIDTH
    new_size_y: int = round(size[1]/(size[0]/new_size_x))

    for frame_filename in all_frames:
        image_file_path: str = c.FRAMES_FP + frame_filename

        frame = open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        File.delete_if_extant(image_file_path)
        frame.save(image_file_path)

        bar.next()

    bar.finish()

    print("All frames resized")
    print(f"Original resolution: {size[0]} x {size[1]}")
    print(f"New resolution: {new_size_x} x {new_size_y}")
    print()
