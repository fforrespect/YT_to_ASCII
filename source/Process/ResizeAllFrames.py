from os import listdir, remove
from PIL.Image import open, Image
from progress.bar import Bar

from Meta import Constants as c


def process() -> None:
    all_frames: list[str] = listdir(c.frames_fp)
    all_frames = list(filter(lambda x: x[-4:] == c.frame_ext, all_frames))

    bar = Bar(
        "Resizing Frames",
        max=len(all_frames),
        fill='█',
        suffix="%(index)d/%(max)d - %(percent).1f%% - %(eta)ds"
    )

    frame: Image = open(c.frames_fp + all_frames[0])
    size: tuple[int, int] = frame.size

    new_size_x: int = c.width
    new_size_y: int = round(size[1]/(size[0]/new_size_x))

    for frame_filename in all_frames:
        image_file_path: str = c.frames_fp + frame_filename

        frame = open(image_file_path)
        frame = frame.resize((new_size_x, new_size_y))
        try: remove(image_file_path)
        except FileNotFoundError: pass
        frame.save(image_file_path)

        bar.next()

    bar.finish()

    print("All frames resized")
    print("Video resolution:", (new_size_x, new_size_y))
    print()
