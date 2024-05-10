from typing import Pattern, Iterator, Match, Any

import re
from os import system
from sys import stdout
from time import time, sleep

from Meta import Constants as c, GlobalVars as gv


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


def get_frame_colours_from_raw_frame_strings_file(fp: str) -> list[list[int]]:
    with open(fp, "r") as strings_file:
        frame_strings: list[str] = "".join(strings_file.readlines()).split(c.DELIMITER)
    
    frame_raw_colours: list[list[str]] = list(map(
        lambda frame: frame.replace("\n", "").split(c.FILL_CHAR),
        frame_strings
    ))
    
    frame_raw_colours = [[colour for colour in frame if colour != ""] for frame in frame_raw_colours]
    
    frame_colours: list[list[int]] = list(map(
        lambda frame: list(map(lambda colour: int(colour[7:-1]), frame)),
        frame_raw_colours
    ))
    
    return frame_colours


def compress_colours() -> list[list[tuple[tuple[int, int], int]]]:
    frame_colours: list[list[int]] = get_frame_colours_from_raw_frame_strings_file(c.STRINGS_FP)
    #           frames  changes  change  coords  x, y     colour
    change_log: list[   list[    tuple[  tuple[int, int], int]]] = []
    
    prev_frame: list[int] = [-1 for _ in frame_colours[0]]
    
    for frame in frame_colours:
        change_log.append([])
        for colour_no, (new_colour, prev_colour) in enumerate(zip(frame, prev_frame)):
            if new_colour != prev_colour:
                coords: tuple[int, int] = colour_no % c.DISPLAY_WIDTH, colour_no // c.DISPLAY_WIDTH
                change_log[-1].append((coords, new_colour))
            
        prev_frame = frame
        
    return change_log
    
    
# INCOMPLETE!!!
def decompress_and_draw():
    compressed_frames = gv.compressed_frames
    
    system("clear")
    print(("**"*c.DISPLAY_WIDTH + '\n') * gv.display_height)
    
    frame_time: float = 1 / c.NEW_FPS
    next_frame_time: float = time() + frame_time
    
    for frame in compressed_frames:
        for change in frame:
            _set_colour(change[0][1], change[0][0]*2, change[1])
        
        sleep_time: float = next_frame_time - time()
        sleep(max(sleep_time, 0))
        next_frame_time += frame_time
    

def _set_colour(row: int, column: int, colour_256):
    # move the cursor to the coords and print the new colour
    stdout.write(f"\033[{row+1};{column+1}H\033[48;5;{colour_256}m{c.FILL_CHAR}\033[0m")
    # Flush to ensure the output is immediately visible
    stdout.flush()


def _clear_character(row, column):
    # move the cursor to the coords and print a zero-width space
    stdout.write(f"\033[{row+1};{column+1}H\u200B")
    # Flush to ensure the output is immediately visible
    stdout.flush()
