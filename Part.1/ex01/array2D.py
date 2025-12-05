import numpy as numpy


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array.

Args:
    family: 2D array
    start: start index
    end: end index

Returns:
    sliced 2D array
"""
    if len(family) == 0:
        raise ValueError("Family must be a non-empty list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers")
    if not isinstance(family, list) or \
       not all(isinstance(row, (list)) for row in family):
        raise ValueError("Family must be a list of lists")
    length = len(family[0])
    if not all(len(row) == length for row in family):
        raise ValueError("All rows of Family must have the same length")
    array = numpy.array(family)
    if array.ndim != 2:
        raise ValueError("Family must be a 2D array")
    print(f"My shape is : ({len(family)}, {length})")
    new_family = array[start:end]
    print(f"My new shape is : ({len(new_family)}, {length})")
    return new_family.tolist()


def main():
    """Main function to test the slice_me function.
    """
    print("=== Normal test case ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test with negative indices ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 1, -2))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test with slice to end ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 2, 4))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test with start > end ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 3, 2))
        print("✓ Test passed (returns empty list)\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test ValueError: start is not an int ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7]]
        slice_me(family, "0", 2)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: end is not an int ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7]]
        slice_me(family, 0, 2.5)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: family is not a list ===")
    try:
        family = "not a list"
        slice_me(family, 0, 2)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: family contains non-list elements ===")
    try:
        family = [[1.80, 78.4],
                  "not a list",
                  [2.10, 98.5]]
        slice_me(family, 0, 2)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: rows have different lengths ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7, 50],
                  [2.10, 98.5]]
        slice_me(family, 0, 2)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test with larger array ===")
    try:
        family = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12],
                  [13, 14, 15]]
        print(slice_me(family, 1, 4))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test with out of bounds indices ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7]]
        print(slice_me(family, 0, 10))
        print("✓ Test passed (Python handles out of bounds)\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test with negative start ===")
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, -3, -1))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")


if __name__ == "__main__":
    main()
