import numpy as numpy
from PIL import Image
from load_image import ft_load


def zoom(array: numpy.ndarray, sizeY: int, sizeX: int,
         centerY: int, centerX: int) -> numpy.ndarray:
    """Zoom an image.
    Args:
        array: Image array (height, width, channels)
        sizeY: Height of the zoom region
        sizeX: Width of the zoom region
        centerY: Starting row (Y position)
        centerX: Starting column (X position)

    Returns:
        Cropped/zoomed image array
    """
    if not isinstance(array, numpy.ndarray):
        raise ValueError("Array must be a numpy ndarray")
    if len(array) == 0:
        raise ValueError("Array must be a non-empty numpy ndarray")
    if not isinstance(sizeY, int):
        raise ValueError("SizeY must be an integer")
    if not isinstance(sizeX, int):
        raise ValueError("SizeX must be an integer")
    if not isinstance(centerY, int):
        raise ValueError("CenterY must be an integer")
    if not isinstance(centerX, int):
        raise ValueError("CenterX must be an integer")
    if array.ndim != 3:
        raise ValueError("Array must be a 3D numpy ndarray")
    try:
        y_start = centerY - sizeY // 2
        y_end = centerY + sizeY // 2
        x_start = centerX - sizeX // 2
        x_end = centerX + sizeX // 2
        new_array = array[y_start:y_end, x_start:x_end]
        new_image = Image.fromarray(new_array)
        new_image = new_image.convert("L")
        gray_array = numpy.array(new_image)
        gray_array = gray_array[:, :, numpy.newaxis]
        print(f"New shape after slicing: {gray_array.shape}")
        new_image.show()
    except Exception as e:
        raise ValueError(f"Error zooming image: {e}")

    return gray_array


def main():
    """Main function to test the zoom function.
    """
    try:
        array = ft_load("animal.jpeg")
        print((array))
        zoomed_array = zoom(array, 400, 400, 290, 650)
        print(zoomed_array)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
