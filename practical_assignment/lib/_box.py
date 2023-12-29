import numpy as np
import cv2


# find the coordinate bounding box of a given label in a components image
def find_bounding_box_from(
        image_: np.ndarray,
        /,
        *,
        label: int
) -> tuple[int, int, int, int]:
    if image_.ndim != 2:
        raise ValueError(
            f"image must be a 2D numpy array, which has {image_.ndim} dimensions."
        )

    # If image.shape is (750, 758), then
    # The created xx looks like this:
    # [[0, 1, 2, ..., 757],
    #  [0, 1, 2, ..., 757],
    #  [0, 1, 2, ..., 757],
    #  ...,
    #  [0, 1, 2, ..., 757],
    #  [0, 1, 2, ..., 757],
    #  [0, 1, 2, ..., 757]]
    #
    # And the created yy looks like this:
    # [[0, 0, 0, ..., 0],
    #  [1, 1, 1, ..., 1],
    #  [2, 2, 2, ..., 2],
    #  ...,
    #  [747, 747, 747, ..., 747],
    #  [748, 748, 748, ..., 748],
    #  [749, 749, 749, ..., 749]]
    xx, yy = np.meshgrid(
        np.arange(0, image_.shape[1]),
        np.arange(0, image_.shape[0])
    )

    # The reason why we do this, is because we want to find the coordinates of the pixels
    # that have the same label as the given label.
    # For example, if the given label is 1,
    # then we want to find the coordinates of the pixels that have the label 1.
    # And we can do this by comparing the image_ with the given label.
    #
    # The results in where_x and where_y are
    # the coordinates of the pixels that have the given label.
    # So we can realize the coordinates of each picked pixel.
    where_x = xx[image_ == label]
    where_y = yy[image_ == label]

    # find min and max extents of coordinates
    return np.min(where_x), np.min(where_y), np.max(where_x), np.max(where_y)


# rotate each of the image according to the central line.
# the central line will become straight and perpendicular to vertical after rotation.
# Rotate along the axis so that the slope of the axis becomes infinite.
# If the slope of the original axis is positive, it rotates counterclockwise; if it is negative, it rotates clockwise.
def rotate_image(
        img: np.ndarray,
        central_line_: [[float, float], [float, float]],
        centroid_: [float, float],
) -> np.ndarray:
    a, b = central_line_

    ax, ay = a
    bx, by = b

    # Calculate the angle of the central line
    angle = np.arctan2(by - ay, bx - ax) * 180 / np.pi

    # rotate the image by the angle, in clockwise direction
    # the center of rotation is the center of the image
    return cv2.warpAffine(
        src=img,
        M=cv2.getRotationMatrix2D(
            (centroid_[0], centroid_[1]), angle - 90, 1.0
        ),
        dsize=(img.shape[1], img.shape[0])
    )
