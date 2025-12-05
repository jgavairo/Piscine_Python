class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1, V2: list[float]) -> None:
        """Dot product of two calculators"""
        print("Dot product is:", sum(a * b for a, b in zip(V1, V2)))

    @staticmethod
    def add_vec(V1, V2: list[float]) -> None:
        """Add two calculators"""
        print("Add Vector is :", [float(a + b) for a, b in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1, V2: list[float]) -> None:
        """Subtract two calculators"""
        print("Sous Vector is:", [float(a - b) for a, b in zip(V1, V2)])
