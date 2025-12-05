class calculator():
    """Calculator class"""

    def __init__(self, values: list[float]) -> None:
        """Calculator constructor"""
        self.values = values

    def __sub__(self, other: float | int) -> None:
        """Subtract two calculators"""
        self.values = [value - other for value in self.values]
        print(self.values)

    def __add__(self, other: float | int) -> None:
        """Add two calculators"""
        self.values = [value + other for value in self.values]
        print(self.values)

    def __mul__(self, other: float | int) -> None:
        """Multiply two calculators"""
        self.values = [value * other for value in self.values]
        print(self.values)

    def __truediv__(self, other: float | int) -> None:
        """Divide two calculators"""
        if other == 0:
            print("Cannot divide by zero")
        else:
            self.values = [value / other for value in self.values]
            print(self.values)
