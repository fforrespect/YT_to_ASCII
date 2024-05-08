from PIL import Image
from numpy import array, ndarray

from Meta.ColourTools import get_bg_colour_setter, get_colour_resetter, colours_equal

greys_ = (' ', '.', '-', '"', 'r', '/', '>', ')', '[', 'I', 'Y', 'Z', 'h', '#', '8', '@')

reset: str = get_colour_resetter()
fill_char: str = " " * 2


def image_to_string(
        file_path: str,
        in_colour: bool = True,
        greys: list[str] = greys_,
        compressed: bool = True) -> str:
    """
    Convert an image to ASCII art.

    :param file_path: Path to the image file.
    :type file_path: str
    :param in_colour: Should the ASCII art be returned in colour or not?
    :type in_colour: bool
    :param greys: A tuple of characters representing greyscale values.
    :type greys: tuple
    :param compressed: Should the coloured output be compressed?
    :type compressed: bool

    :returns ASCII art representation of the image
    :rtype str
    """

    image: Image.Image = Image.open(file_path)
    image_array: ndarray = array(image)
    
    if in_colour:
        output = "\n".join([
            "".join([
                (
                    "".join([get_bg_colour_setter(pixel_colour), fill_char])
                    if not compressed and
                       (current_colour is None or not colours_equal(pixel_colour, current_colour))
                    else fill_char
                ) for pixel_colour, current_colour in zip(row, [None] + list(row[:-1]))
            ]) for row in image_array
        ])
    
    else:
        greyscale: bool = len(image_array.shape) == 2
        
        colour_scale: int = len(greys) - 1
        normalised_image: ndarray = (image_array.mean(axis=2) / 255 * colour_scale if not greyscale
                                     else image_array / 255 * colour_scale).astype(int)
        
        output = "\n".join("".join(greys[val] * 2 for val in row) for row in normalised_image)
    
    return output


if __name__ == "__main__":
    print(image_to_string("../resources/images/rose.png"))
    print("hi")
