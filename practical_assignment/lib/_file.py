from typing import Final

import numpy as np
from PIL import Image


class _FileAgent:
    __data_dir: Final[str]
    __RESISTOR_DIR_NAME: Final[str] = "RESISTORS"
    __COMPONENTS_DIR_NAME: Final[str] = "COMPONENTS"
    __BOARDS_DIR_NAME: Final[str] = "BOARDS"
    __ANNOTATION_DIR_NAME: Final[str] = "ANNOTATIONS"

    def __init__(self, *, data_dir: str):
        self.__data_dir = data_dir

    @property
    def resistor_dir(self) -> str:
        return f"{self.__data_dir}/{self.__RESISTOR_DIR_NAME}"

    @property
    def components_dir(self) -> str:
        return f"{self.__data_dir}/{self.__COMPONENTS_DIR_NAME}"

    @property
    def boards_dir(self) -> str:
        return f"{self.__data_dir}/{self.__BOARDS_DIR_NAME}"

    @property
    def annotation_dir(self) -> str:
        return f"{self.__data_dir}/{self.__ANNOTATION_DIR_NAME}"

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
