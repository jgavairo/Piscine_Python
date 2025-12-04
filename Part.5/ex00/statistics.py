from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate the statistics of the given arguments.

    Args:
        *args: The arguments to calculate the statistics of.
        **kwargs: The keyword arguments to calculate the statistics of.
    """
    if not args:
        print("ERROR: No arguments provided")
        return
    if not kwargs:
        print("ERROR: No keyword arguments provided")
        return
    for arg in args:
        if not isinstance(arg, (int, float)):
            print("ERROR: Arguments must be int or float")
            return
    for key, value in kwargs.items():
        if key not in ["mean", "median", "quartile"]:
            print("ERROR: Keyword arguments must be mean, median, or quartile")
            return
    
    