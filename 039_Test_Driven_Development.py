# Test Driven Develovelopment is a software development approach where tests are written before the code that needs to be tested. This ensures that the code meets the requirements and behaves as expected from the start.
# The Test-Driven Development (TDD) process typically follows these steps:
# Write a failing test for a new feature or functionality.
# Writing the minimum amount of code necessary to pass the test.
# Refactor the code to make it easier to understand and maintain.
# Example of Test Driven Development using unittest in Python:
import unittest


def add(a, b):
    """Return the sum of a and b."""
    return a + b


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(
            add(2, 3), 6
        )  # This test will fail because the expected result is incorrect.


if __name__ == "__main__":
    unittest.main()


# In this example, the test `test_add_positive_numbers` is expected to fail because the expected result is incorrect (it should be 5, not 6). The next step in TDD would be:
# Write the minimum amount of code necessary to pass the test:
# Example:
def add(a, b):
    """Return the sum of a and b."""
    return a + b


# In the second phase, the goal is to make the test pass by correcting the expected result in the test case:
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)  # Now the expected result is correct.


# After making the test pass, you can refactor the code if necessary. In this case, the `add` function is already simple and does not require refactoring.
# The goal is t keep the code clean, removing duplication, improving naming and applying design principles as needed.

# Repeating the process, you can add more tests for different scenarios, such as adding negative numbers or zero, and ensure that the `add` function behaves correctly in all cases.
