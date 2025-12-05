from load_image import ft_load
from PIL import Image
import numpy as numpy


def ft_invert(array: numpy.ndarray) -> numpy.ndarray:
    """Invert the colors of an image.
    """
    if not isinstance(array, numpy.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        new_array = 255 - array
        new_image = Image.fromarray(new_array)
        new_image.show()
        return new_array
    except Exception as e:
        raise ValueError(f"Error making image invert: {e}")


def ft_red(array: numpy.ndarray) -> numpy.ndarray:
    """Make the image red.
    """
    if not isinstance(array, numpy.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        new_array = array.copy()
        new_array[:, :, 1] *= 0
        new_array[:, :, 2] *= 0
        new_image = Image.fromarray(new_array)
        new_image.show()
    except Exception as e:
        raise ValueError(f"Error making image red: {e}")

    return new_array


def ft_green(array: numpy.ndarray) -> numpy.ndarray:
    """Make the image green.
    """
    if not isinstance(array, numpy.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        new_array = array.copy()

        new_array[:, :, 0] -= new_array[:, :, 0]
        new_array[:, :, 2] -= new_array[:, :, 2]

        new_image = Image.fromarray(new_array)
        new_image.show()
    except Exception as e:
        raise ValueError(f"Error making image green: {e}")

    return new_array


def ft_blue(array: numpy.ndarray) -> numpy.ndarray:
    """Make the image blue.
    """
    if not isinstance(array, numpy.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        new_array = array.copy()
        new_array[:, :, 0] = 0
        new_array[:, :, 1] = 0
        new_image = Image.fromarray(new_array)
        new_image.show()
    except Exception as e:
        raise ValueError(f"Error making image blue: {e}")

    return new_array


def ft_grey(array: numpy.ndarray) -> numpy.ndarray:
    """Make the image grey.
    """
    if not isinstance(array, numpy.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        new_array = array.copy()

        grey = new_array.sum(axis=2) / 3
        new_array[:, :, 0] = grey
        new_array[:, :, 1] = grey
        new_array[:, :, 2] = grey

        new_image = Image.fromarray(new_array)
        new_image.show()
    except Exception as e:
        raise ValueError(f"Error making image grey: {e}")

    return new_array


def main():
    """Main function to test the pimp_image functions.
    """
    try:
        array = ft_load("landscape.jpg")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
