color_cache = {}


def _rgb_to_256colour(rgb: tuple[int, int, int]) -> int:
    rgb = tuple(map(int, rgb))

    if rgb in color_cache:
        return color_cache[rgb]

    r, g, b = rgb
    result = 16 + ((r * 5) // 256 * 36) + ((g * 5) // 256 * 6) + (b * 5) // 256
    color_cache[rgb] = result
    return result


def colours_equal(colour1: tuple[int, int, int], colour2: tuple[int, int, int]) -> bool:
    return _rgb_to_256colour(colour1) == _rgb_to_256colour(colour2)


def get_text_colour_setter(colour: tuple[int, int, int]) -> str:
    return f"\033[38;5;{_rgb_to_256colour(colour)}m"


def get_bg_colour_setter(colour: tuple[int, int, int]) -> str:
    return f"\033[48;5;{_rgb_to_256colour(colour)}m"


def get_colour_resetter() -> str:
    return "\033[0m"


def get_coloured_string(text: str,
                        text_colour: tuple[int, int, int] | None = None,
                        background_colour: tuple[int, int, int] | None = None) -> str:
    set_text_colour: str = get_text_colour_setter(text_colour) if text_colour is not None else ""
    set_bg_colour: str = get_bg_colour_setter(background_colour) if background_colour is not None else ""
    return f"{set_text_colour}{set_bg_colour}{text}{get_colour_resetter()}"


def printc(text: str,
           text_colour: tuple[int, int, int] | None = None,
           background_colour: tuple[int, int, int] | None = None) -> None:
    print(get_coloured_string(text, text_colour, background_colour))


if __name__ == "__main__":
    printc("test")
    printc("test", (255,   0, 0))
    printc("test", background_colour=(255,   0, 0))
    printc("test", (255,   0,   0), (  0,   0, 255))
