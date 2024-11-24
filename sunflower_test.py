
import unittest
from unittest.mock import MagicMock
from sunflower import draw_sunflower

class TestTurtleGraphics(unittest.TestCase):

    def test_draw_sunflower(self):
        mock_turtle = MagicMock()
        draw_sunflower(mock_turtle, 18)

        self.assertEqual(mock_turtle.circle.call_count, 37)
        self.assertEqual(mock_turtle.left.call_count, 36)
        self.assertEqual(mock_turtle.right.call_count, 18)

        mock_turtle.left.assert_called_with(120)
        mock_turtle.right.assert_called_with(20)

if __name__ == "__main__":
    unittest.main()
