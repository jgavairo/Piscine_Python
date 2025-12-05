from typing import Any


def is_valid_args(args, starting_program: bool = False) -> bool:
    """
    Verify the arguments are valid.
    """

    if starting_program:
        for arg in args:
            if not isinstance(arg, (int, float)):
                return False
        return True

    if not args:
        print("ERROR")
        return False
    return True


def calculate_mean(args, print_result: bool = True) -> float:
    """
    Calculate the mean of the given arguments.
    """
    mean = sum(args) / len(args)
    if print_result:
        print("mean :", mean)
    return mean


def calculate_median(args: list[int | float]) -> float:
    """
    Calculate the median of the given arguments.
    """
    if len(args) % 2 == 0:
        mid = len(args) // 2
        median = (sorted(args)[mid] + sorted(args)[mid - 1]) / 2
    else:
        median = sorted(args)[len(args) // 2]
    print("median :", median)


def calculate_quartile(args: list[int | float]) -> tuple[int, int]:
    """
    Calculate the quartile of the given arguments.
    """
    sorted_args = sorted(args)

    q1_index = int(0.25 * (len(sorted_args) - 1))
    q3_index = int(0.75 * (len(sorted_args) - 1))

    q1 = sorted_args[q1_index]
    q3 = sorted_args[q3_index]
    print(f"quartile : [{float(q1)}, {float(q3)}]")
    return q1, q3


def calculate_var(args: list[int | float], print_result: bool = True) -> float:
    """
    Calculate the variance of the given arguments.
    """
    n = len(args)
    mean = calculate_mean(args, print_result=False)
    var = sum((x - mean) ** 2 for x in args) / n

    if print_result:
        print("var :", var)
    return var


def calculate_std(args: list[int | float]) -> float:
    """
    Calculate the standard deviation of the given arguments.
    """
    std = calculate_var(args, print_result=False) ** 0.5
    print("std :", std)
    return std


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate the statistics of the given arguments.

    Args:
        *args: The arguments to calculate the statistics of.
        **kwargs: The keyword arguments to calculate the statistics of.
    """
    if not is_valid_args(args, starting_program=True):
        return

    for value in kwargs.values():
        if value not in ["mean", "median", "quartile", "std", "var"]:
            continue
        if value == "mean":
            if is_valid_args(args):
                calculate_mean(args)
                continue
        if value == "median":
            if is_valid_args(args):
                calculate_median(args)
                continue
        if value == "quartile":
            if is_valid_args(args):
                calculate_quartile(args)
                continue
        if value == "var":
            if is_valid_args(args):
                calculate_var(args)
                continue
        if value == "std":
            if is_valid_args(args):
                calculate_std(args)
                continue
