def square(x: int | float) -> int | float:
    """Square function"""
    if not isinstance(x, (int, float)):
        print("ERROR: argument is not a number")
        return None
    return x * x


def pow(x: int | float) -> int | float:
    """Pow function"""
    if not isinstance(x, (int, float)):
        print("ERROR: argument is not a number")
        return None
    return x ** x


def outer(x: int | float, function) -> object:
    """Outer function"""
    count = 0
    result = x

    if not function or not callable(function):
        print("ERROR: function is not a function")
        return None

    def inner() -> float:
        """Inner function"""
        nonlocal count, result

        if count == 0:
            result = function(x)
        else:
            result = function(result)

        count += 1

        return result

    return inner
