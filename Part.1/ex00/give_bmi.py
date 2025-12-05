

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI of a person given their height and weight.

Args:
    height: list of heights in meters
    weight: list of weights in kilograms

Returns:
    list of BMIs
"""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists")

    if len(height) != len(weight):
        raise ValueError("Height and weight must have the same length")

    for i in range(len(height)):
        if not isinstance(height[i], (int, float)) or \
           not isinstance(weight[i], (int, float)):
            raise TypeError("Height and weight must be lists of int or float")
        if height[i] <= 0 or weight[i] <= 0:
            raise ValueError("Height and weight must be more than 0")

    return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to a list of BMIs.

Args:
    bmi: list of BMIs
    limit: limit to apply

Returns:
    list of booleans
"""
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("BMI and limit must be lists of int or float")
    return [bmi[i] > limit for i in range(len(bmi))]


def main():
    """Main function to test the give_bmi and apply_limit functions.
    """
    print("=== Normal test case ===")
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
        print("✓ Test passed\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")

    print("=== Test TypeError: height is not a list ===")
    try:
        height = "not a list"
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except TypeError as e:
        print(f"✓ TypeError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test TypeError: weight is not a list ===")
    try:
        height = [2.71, 1.15]
        weight = 165.3
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except TypeError as e:
        print(f"✓ TypeError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: different lengths ===")
    try:
        height = [2.71, 1.15, 1.80]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test TypeError: invalid elements ===")
    try:
        height = [2.71, "1.15"]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except TypeError as e:
        print(f"✓ TypeError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: negative value ===")
    try:
        height = [2.71, -1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test ValueError: zero value ===")
    try:
        height = [2.71, 1.15]
        weight = [165.3, 0]
        bmi = give_bmi(height, weight)
        print("✗ Error not detected\n")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test TypeError apply_limit: bmi is not a list ===")
    try:
        apply_limit("not a list", 26)
        print("✗ Error not detected\n")
    except TypeError as e:
        print(f"✓ TypeError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")

    print("=== Test TypeError apply_limit: limit is not an int ===")
    try:
        bmi = [22.5, 29.0]
        apply_limit(bmi, 26.5)
        print("✗ Error not detected\n")
    except TypeError as e:
        print(f"✓ TypeError caught: {e}\n")
    except Exception as e:
        print(f"✗ Wrong exception: {e}\n")


if __name__ == "__main__":
    main()
