import unittest
from task import Circle, Triangle


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.circle1 = Circle(5)
        self.circle2 = Circle(3.4)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle1.get_area(), 78.54, places=2)
        self.assertAlmostEqual(self.circle2.get_area(), 36.32, places=2)


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle1 = Triangle([3, 4, 5])
        self.triangle2 = Triangle([2, 3, 4])

    def test_triangle_area(self):
        self.assertAlmostEqual(self.triangle1.get_area(), 6.0, places=2)
        self.assertAlmostEqual(self.triangle2.get_area(), 2.9, places=2)

    def test_is_right_triangle(self):
        self.assertTrue(self.triangle1.is_right())
        self.assertFalse(self.triangle2.is_right())


if __name__ == '__main__':
    unittest.main()
