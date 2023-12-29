import cv2
import numpy as np
from matplotlib import pyplot as plt


def show_images_in_row(images: [np.ndarray], /, *, fig_size: tuple[int, int] = (20, 5)) -> None:
    _, _axs = plt.subplots(1, len(images), figsize=fig_size)
    for n, component in enumerate(images):
        _axs[n].imshow(component)
        _axs[n].set_title(f'Resistor {n + 1}')

    plt.show()


def draw_central_line_on(
        img: np.ndarray, /, *, a: [float, float], b: [float, float]
) -> np.ndarray:
    return cv2.line(img, (int(a[0]), int(a[1])), (int(b[0]), int(b[1])), (0, 0, 255), 2)


def show_vertical_rgb_analysis_of(result: np.ndarray, /, *, label: str) -> None:
    if result.shape[0] != 3:
        raise ValueError("The analysis result should have 3 layers.")

    colors = ('r', 'g', 'b')
    plt.figure(figsize=(20, 5))
    plt.title(f"Color distribution of {label}")
    for layer in range(3):
        plt.plot(result[layer], color=colors[layer], label=f"Layer {colors[layer]}")

    plt.legend()
    plt.show()
