from __future__ import annotations

from enum import Enum, unique
from collections.abc import Sequence


@unique
class ResistorColor(Enum):
    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GRAY = 8
    WHITE = 9
    GOLD = 10
    SILVER = 11
    NONE = 12


class ResistorColorFinder:
    __black_rgb_range = (range(0, 73), range(0, 73), range(0, 73),)
    __brown_rgb_range = (range(92, 171), range(48, 122), range(23, 97),)
    __red_rgb_range = (range(213, 225), range(48, 105), range(58, 110),)
    __orange_rgb_range = (range(200, 240), range(105, 130), range(50, 100),)
    __yellow_rgb_range = (range(225, 235), range(185, 195), range(5, 8),)
    __green_rgb_range = (range(8, 15), range(80, 90), range(45, 50),)
    __blue_rgb_range = None  # there's no blue bands.
    __violet_rgb_range = (range(195, 197), range(135, 145), range(180, 185),)
    __gray_rgb_range = None  # there's no gray bands.
    __white_rgb_range = (range(185, 255), range(185, 255), range(185, 255),)

    # __gold_rgb_range = (range(130, 230), range(90, 225), range(54, 225),)
    # __silver_rgb_range = (range(195, 205), range(195, 205), range(195, 205),)

    @classmethod
    def from_rgb(cls, rgb: Sequence[int, int, int]) -> ResistorColor:
        all_ranges = (
            cls.__black_rgb_range,
            cls.__brown_rgb_range,
            cls.__red_rgb_range,
            cls.__orange_rgb_range,
            cls.__yellow_rgb_range,
            cls.__green_rgb_range,
            cls.__blue_rgb_range,
            cls.__violet_rgb_range,
            cls.__gray_rgb_range,
            cls.__white_rgb_range,
        )

        for i, color_ranges in enumerate(all_ranges):
            if color_ranges is None:
                continue

            if all([
                    rgb[0] in color_ranges[0],
                    rgb[1] in color_ranges[1],
                    rgb[2] in color_ranges[2],
            ]):
                return ResistorColor(i)
        else:
            if len(set(rgb)) == 1:
                return ResistorColor.SILVER
            else:
                return ResistorColor.GOLD

