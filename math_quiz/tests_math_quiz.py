import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):
    """Unit tests for functions in the math quiz module."""

    def test_function_A(self):
        """Test if function_A generates a random number within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values for reliability
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val,
                            f"Generated number {rand_num} is out of range ({min_val}, {max_val})")

    def test_function_B(self):
        """Test function_B with various valid and invalid inputs to ensure correct behavior."""
        # Placeholder example, adjust based on function_B's actual purpose
        example_input = 5
        expected_output = 10  # Adjust as needed for actual function behavior
        self.assertEqual(function_B(example_input), expected_output,
                         "function_B did not return the expected result.")

    def test_function_C(self):
        """Test function_C's response to both correct and incorrect inputs."""
        correct_input = "correct"
        incorrect_input = "incorrect"
        self.assertTrue(function_C(correct_input),
                        "function_C should return True for correct input.")
        self.assertFalse(function_C(incorrect_input),
                         "function_C should return False for incorrect input.")


if __name__ == '__main__':
    unittest.main()
