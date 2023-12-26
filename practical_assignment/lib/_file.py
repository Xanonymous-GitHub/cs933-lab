from typing import Final

import numpy as np
from PIL import Image


class _FileAgent:
    __data_dir: Final[str]

    def __init__(self, *, data_dir: str):
        self.__data_dir = data_dir

    def get_img_located_at(
            self,
            location_of_image: str,
            /,
            *,
            channel_mode: str | None = None,
    ) -> np.ndarray:
        """
        Get the image named `name_of_image` from the data directory.
        """
        img = Image.open(f"{self.__data_dir}/{location_of_image}")

        if channel_mode is not None:
            img = img.convert(channel_mode)

        return np.asarray(img)
