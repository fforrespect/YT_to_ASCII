from PIL import Image
import numpy as np

greys = (' ', '.', '-', '"', 'r', '/', '>', ')', '[', 'I', 'Y', 'Z', 'h', '#', '8', '@')


def image_to_string(image_file_path, colours=greys):
    """
    Convert an image to ASCII art.

    Parameters:
    image_file_path (str): Path to the image file.
    in_place (bool): If True, prints the ASCII art. If False, returns the ASCII art as a string.
    colours (tuple): A tuple of characters representing grayscale values.

    Returns:
    str: ASCII art representation of the image (if in_place is False).
    """
    image = Image.open(image_file_path)
    image_array = np.array(image)
    greyscale = len(image_array.shape) == 2

    colour_scale = len(colours) - 1
    normalised_image = (image_array.mean(axis=2) / 255 * colour_scale if not greyscale
                        else image_array / 255 * colour_scale).astype(int)

    return "\n".join("".join(colours[val] * 2 for val in row) for row in normalised_image)
