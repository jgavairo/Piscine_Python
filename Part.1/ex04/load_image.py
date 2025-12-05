from PIL import Image
import numpy as numpy


def ft_load(path: str) -> numpy.ndarray:
    """Load an image from a file.
    """
    if not isinstance(path, str):
        raise ValueError("Path must be a string")
    try:
        image = Image.open(path)
        img = image.convert("RGB")
        array = numpy.array(img)
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

    return array


def main():
    """Main function to test the ft_load function.
    """
    try:
        print(ft_load("landscape.jpg"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
