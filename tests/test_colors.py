import unittest
from src.colors import add, blend, fade, BLACK, GRAY


class TestBlendFunction(unittest.TestCase):

    def test_blend_colors(self):
        # Test case 1
        result = blend((255, 0, 0), (0, 255, 0), 50)
        self.assertEqual(result, (127.5, 127.5, 0))

        # Test case 2
        result = blend((255, 0, 0), (0, 0, 255), 25)
        self.assertEqual(result, (191.25, 0.0, 63.75))

    def test_invalid_input(self):
        # Test case for invalid input
        result = blend((255, 0, 0), (0, 255, 0, 255), 50)
        self.assertEqual(result, GRAY)


class TestFadeFunction(unittest.TestCase):

    def test_fade_color(self):
        # Test case 1
        result = fade((255, 0, 0), 50)
        self.assertEqual(result, (127.5, 0, 0))

        # Test case 2
        result = fade((0, 255, 0), 25)
        self.assertEqual(result, (0, 63.75, 0))

    def test_fade_to_black(self):
        # Test case for fading to black
        result = fade((100, 150, 200), 0)
        self.assertEqual(result, BLACK)  # Fading with ratio 100 should result in black

    def test_invalid_input(self):
        # Test case for invalid input
        result = fade((255, 0, 0, 255), 50)
        self.assertEqual(result, GRAY)  # Invalid color should fade to black


class TestAddFunction(unittest.TestCase):
    def test_adding_colors(self):
        # Test case 1
        result = add((100, 50, 25), (50, 75, 30))
        self.assertEqual(result, (150, 125, 55))

        # Test case 2
        result = add((200, 100, 50), (30, 40, 60))
        self.assertEqual(result, (230, 140, 110))

        # Test case 3
        result = add((255, 255, 255), (0, 0, 0))
        self.assertEqual(result, (255, 255, 255))

    def test_color_constraining(self):
        # Test case 1
        result = add((200, 150, 100), (100, 150, 200))
        self.assertEqual(result, (255, 255, 255))  # All components should be constrained to 255

        # Test case 2
        result = add((300, 0, 0), (0, 0, 300))
        self.assertEqual(result, (255, 0, 255))  # Red and blue components should be constrained to 255

    def test_empty_input(self):
        # Test case for an empty input
        result = add()
        self.assertEqual(result, (0, 0, 0))  # Sum of an empty list should be (0, 0, 0)


if __name__ == '__main__':
    unittest.main()
