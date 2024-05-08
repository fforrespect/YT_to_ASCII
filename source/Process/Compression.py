from typing import Pattern, Iterator, Match

import re
from os import system
from sys import stdout

from Meta import Constants as c, ColourTools as ct


def _find_esc_sequences(s: str) -> list[tuple[int, int]]:
    # Regex pattern
    pattern: Pattern[str] = re.compile(r'\x1b\[.*?m')
    # Find the locations of all the colour markers
    matches: Iterator[Match[str]] = pattern.finditer(s)

    # Initialise a variable to keep track of the total length of all previous matches
    total_removed_length: int = 0
    results: list[tuple[int, int]] = []

    # Iterate through all the matches, noting down the 256 colour value,
    #   as well as the adjusted index, which is the index of the start of the colour escape string,
    #   if no previous colour escape strings had existed
    for match in matches:
        # Adjust the index by subtracting the total length of matches found before this one
        adjusted_index: int = match.start() - total_removed_length
        
        match_content: str = match.group()
        _256_colour: int = int(match_content[7:-1])
        
        results.append((adjusted_index, _256_colour))

        # Update the total_removed_length by adding the length of the current match
        total_removed_length += len(match_content)

    return results


def compress_colours() -> list[list[list[tuple[int, int]]]]:
    with open(c.STRINGS_FP, "r") as strings_file:
        # The 'str' in list[list[str]] is a single line in one frame
        frame_strings: list[list[str]] = list(map(
            lambda frame: frame.split("\n"), "".join(strings_file.readlines()).split(c.DELIMITER)
        ))

    compressed_frames: list[list[list[tuple[int, int]]]] = [
        [
            _find_esc_sequences(line)
            for line in frame
        ] for frame in frame_strings
    ]

    return compressed_frames


# INCOMPLETE!!!
def decompress_and_draw(compressed_frames: list[list[list[tuple[int, int]]]]):
    # the tuple represents one line
    system("clear")
    print(("**"*c.DISPLAY_WIDTH + '\n')*len(compressed_frames[0]))


def _set_colour(row: int, column: int, colour_256):
    # move the cursor to the coords and print the new colour
    stdout.write(f"\033[{row+1};{column+1}H{colour_256}")
    # Flush to ensure the output is immediately visible
    stdout.flush()


def _clear_character(row, column):
    # move the cursor to the coords and print a zero-width space
    stdout.write(f"\033[{row+1};{column+1}H\u200B")
    # Flush to ensure the output is immediately visible
    stdout.flush()
