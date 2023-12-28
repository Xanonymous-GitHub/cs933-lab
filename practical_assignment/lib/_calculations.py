import numpy as np
import cv2


def find_centroid_from(image_: np.ndarray, /) -> np.ndarray:
    if image_.ndim != 2:
        raise ValueError(
            f"image must be a 2D numpy array, which has {image_.ndim} dimensions."
        )

    xx, yy = np.meshgrid(
        np.arange(0, image_.shape[1]),
        np.arange(0, image_.shape[0])
    )

    # mask by where im is non-zero
    non_zero_x_points = xx[image_ != 0]
    non_zero_y_points = yy[image_ != 0]

    # return the mean of the coordinates of the component
    return np.array([np.mean(non_zero_x_points), np.mean(non_zero_y_points)])


def find_principal_axes_from(image_: np.ndarray) -> np.ndarray:
    """
    Finds the principal axes of a labeled region in a 2D array (image).
    This function assumes the region of interest is labeled by non-zero values.

    Args:
        image_: 2D numpy array representing an image.

    Returns:
        two points representing the principal axis of the labeled region.
        connect these points to visualize the principal axis.
    """
    # Check that the provided image array is two-dimensional.
    if image_.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")

    # Determine the 'center of mass' for the non-zero pixels in the image.
    centroid_x_, centroid_y_ = find_centroid_from(image_)

    # Generate two arrays representing the x and y coordinates for each pixel.
    xx, yy = np.meshgrid(np.arange(image_.shape[1]), np.arange(image_.shape[0]))

    # Filter out the coordinates of pixels that are zero, and shift the remaining
    # pixel coordinates by the centroid values to center them at the origin (0,0).
    x_shifted = xx[image_ != 0] - centroid_x_
    y_shifted = yy[image_ != 0] - centroid_y_

    # Combine the centered x and y coordinates into a single 2-row array.
    # This forms a set of 2D vectors pointing from the centroid to each non-zero pixel.
    centered_coordinates = np.vstack((x_shifted, y_shifted))

    # Compute the 'inertia tensor' for the distribution of non-zero pixels,
    # which is similar to the covariance matrix but not normalized by the number of pixels.
    inertia_tensor = np.matmul(centered_coordinates, centered_coordinates.T)

    # Solve for the eigenvectors and eigenvalues of the inertia tensor.
    # The eigenvectors represent the directions of the axes of the pixel distribution,
    # and the eigenvalues represent the 'spread' or 'weight' along these axes.
    eigenvalues, eigenvectors = np.linalg.eig(inertia_tensor)

    # Select the eigenvector associated with the largest eigenvalue.
    # This vector represents the principal axis of the distribution,
    # which is the direction along which the pixels are most spread out.
    principal_axis = eigenvectors[0, :] if eigenvalues[0] > eigenvalues[1] else eigenvectors[1, :]

    # From the centroid, extend the principal axis to the edge of the image,
    # and return the coordinates of the two points.
    def get_x_of_principal_axis_line_at(y: float):
        return (y - centroid_y_) / principal_axis[1] * principal_axis[0] + centroid_x_

    return np.array([
        [get_x_of_principal_axis_line_at(0), 0],
        [get_x_of_principal_axis_line_at(image_.shape[0]), image_.shape[0]]
    ], dtype=np.float32)



# Reduce color followed by the ratio.
def reduce_color(img: np.ndarray, /, *, to: int) -> np.ndarray:
    # Reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixels = img.reshape((-1, 3))

    # Convert to float
    pixels = np.float32(pixels)

    # Define criteria, number of clusters(K) and apply k-means()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, to, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert back to 8 bit values
    centers = np.uint8(centers)

    # Map the labels to the centers
    reduced_img = centers[labels.flatten()]

    # Reshape back to the original image dimension
    return reduced_img.reshape(img.shape)
