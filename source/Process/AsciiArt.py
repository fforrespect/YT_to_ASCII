from PIL import Image
from numpy import array, ndarray

greys = (' ', '.', '-', '"', 'r', '/', '>', ')', '[', 'I', 'Y', 'Z', 'h', '#', '8', '@')


def image_to_string(file_path: str, colours: list[str] = greys) -> str:
    """
    Convert an image to ASCII art.

    :param file_path: Path to the image file.
    :type file_path: str
    :param colours: A tuple of characters representing greyscale values.
    :type colours: tuple

    :returns ASCII art representation of the image
    :rtype str
    """

    image: Image.Image = Image.open(file_path)
    # The following line may throw a warning, there's no reason it should - it will always work fine
    # noinspection PyTypeChecker
    image_array: ndarray = array(image)
    greyscale: bool = len(image_array.shape) == 2

    colour_scale: int = len(colours) - 1
    normalised_image: ndarray = (image_array.mean(axis=2) / 255 * colour_scale if not greyscale
                                 else image_array / 255 * colour_scale).astype(int)

    return "\n".join("".join(colours[val] * 2 for val in row) for row in normalised_image)
