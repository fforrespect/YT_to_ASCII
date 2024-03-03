from typing import Literal


def _rgb_to_256colour(rgb: tuple[int, int, int]) -> int:
    # Quantize RGB values to fit within the ANSI 256-colour space
    quantised_rgb: tuple[int, int, int] = tuple[int, int, int]([round((c / 255) * 5) for c in rgb])
    # Calculate the ANSI 256-colour index
    return 16 + (quantised_rgb[0] * 36) + (quantised_rgb[1] * 6) + quantised_rgb[2]


def colours_equal(colour1: tuple[int, int, int], colour2: tuple[int, int, int]) -> bool:
    return _rgb_to_256colour(colour1) == _rgb_to_256colour(colour2)


def get_colour_setter(colour: tuple[int, int, int], target: Literal['text', 'background'] = 'text') -> str:
    esc_char: int = 4 if target == 'background' else 3
    return f"\033[{esc_char}8;5;{_rgb_to_256colour(colour)}m"


def get_colour_resetter() -> str:
    return "\033[0m"


def get_coloured_string(text: str,
                        text_colour: tuple[int, int, int] | None = None,
                        background_colour: tuple[int, int, int] | None = None) -> str:
    set_text_colour: str = get_colour_setter(text_colour) if text_colour is not None else ""
    set_bg_colour: str = get_colour_setter(background_colour, 'background') if background_colour is not None else ""
    return f"{set_text_colour}{set_bg_colour}{text}{get_colour_resetter()}"


def printc(text: str,
           text_colour: tuple[int, int, int] | None = None,
           background_colour: tuple[int, int, int] | None = None) -> None:
    print(get_coloured_string(text, text_colour, background_colour))


if __name__ == "__main__":
    printc("test")
    printc("test", (255, 0, 0))
    printc("test", background_colour=(255, 0, 0))
    printc("test", (255, 0, 0), (0, 0, 255))
