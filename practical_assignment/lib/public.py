from typing import Final

from ._box import find_bounding_box_from, rotate_image, find_single_components_in, rotate_img_by_angle
from ._file import _FileAgent
from ._presentation import show_images_in_row, draw_central_line_on, show_vertical_rgb_analysis_of
from ._calculations import (
    find_principal_axes_from,
    find_centroid_from,
    central_line_of,
    crop_img_to_fixed_size,
    vertical_color_distribution_of,
    remove_shadow_from,
)
from ._color import ResistorColorFinder, ResistorColor
from ._resistor_value import calculate_resistor_value

__all__ = [
    "db",
    "find_bounding_box_from",
    "show_images_in_row",
    "find_principal_axes_from",
    "find_centroid_from",
    "central_line_of",
    "draw_central_line_on",
    "rotate_image",
    "crop_img_to_fixed_size",
    "find_single_components_in",
    "vertical_color_distribution_of",
    "show_vertical_rgb_analysis_of",
    "remove_shadow_from",
    "rotate_img_by_angle",
    "ResistorColorFinder",
    "ResistorColor",
    "calculate_resistor_value",
]

db: Final[_FileAgent] = _FileAgent(data_dir="data_dir")
