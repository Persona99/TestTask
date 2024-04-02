import math


class Circle:
    def __init__(self, radius: float) -> None:
        self._validate(radius)
        self.radius = radius

    def _validate(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Invalid radius")

    def get_area(self) -> float:
        return math.pi * self.radius**2


class Triangle:
    def __init__(self, sides: list[float]) -> None:
        self._validate(sides)
        self.sides = sides

    def _validate(self, sides: list[float]) -> None:
        if len(sides) != 3:
            raise ValueError("Incorrect sides length")
        if min(sides) <= 0:
            raise ValueError("Side can't be less than or equal to 0")
        if sum(sides) - max(sides) * 2 <= 0:  # Сумма любых двух сторон всегда больше третьей
            raise ValueError('This triangle is imposibble')

    def get_area(self) -> float:  # Использовал формулу Герона
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        area = math.sqrt(
            p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        return area

    def is_right(self) -> bool:
        return self.sides[0]**2 + self.sides[1]**2 == self.sides[2]**2
