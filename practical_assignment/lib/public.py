from typing import Final

import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageEnhance
from skimage import measure
from skimage.restoration import inpaint
from sklearn.cluster import KMeans

from ._box import find_bounding_box_from, rotate_image
from ._file import _FileAgent
from ._presentation import show_images_in_row, draw_central_line_on
from ._calculations import (
    find_principal_axes_from,
    find_centroid_from,
    central_line_of,
    crop_img_to_fixed_size,
)

__all__ = [
    "np",
    "plt",
    "mpl",
    "measure",
    "cv2",
    "db",
    "inpaint",
    "KMeans",
    "ImageEnhance",
    "find_bounding_box_from",
    "show_images_in_row",
    "find_principal_axes_from",
    "find_centroid_from",
    "central_line_of",
    "draw_central_line_on",
    "rotate_image",
    "crop_img_to_fixed_size",
]

db: Final[_FileAgent] = _FileAgent(data_dir="data_dir")
