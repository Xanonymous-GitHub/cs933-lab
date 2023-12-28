from matplotlib import pyplot as plt
from numpy import ndarray


def show_images_in_row(images: [ndarray], /, *, fig_size: tuple[int, int] = (20, 5)) -> None:
    _, _axs = plt.subplots(1, len(images), figsize=fig_size)
    for n, component in enumerate(images):
        _axs[n].imshow(component)
        _axs[n].set_title(f'Resistor {n + 1}')

    plt.show()
