# Unit testing involves testing individual units or components of your code to ensure they work as expected. Python provides several frameworks and libraries for unit testing, such as unittest, pytest, and nose.
# In this example, we will use the unittest framework to create a simple test case for a function that adds two numbers.
import unittest


def add(a, b):
    """Function to add two numbers."""
    return a + b


class TestAddFunction(unittest.TestCase):
    """Test case for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        """Test adding zero to a number."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()


# To run the tests, save this code in a file named `038_unit_testing_with_unittest.py` and execute it. The unittest framework will automatically discover and run the test cases defined in the `TestAddFunction` class.
# If all tests pass, you will see an output indicating that the tests were successful. If any test fails, the output will show which test failed and why, allowing you to debug your code effectively.
# This is a basic example of unit testing in Python using the unittest framework. You can expand this by adding more test cases, testing edge cases, and even mocking dependencies if needed. Unit testing is a crucial part of software development that helps ensure code quality and reliability.
# Some common assertion methods include: assertEqual(), assertNotEqual(), assertTrue(), assertFalse(), assertIsNone(), and assertRaises().
# You can also use setUp() and tearDown() methods to prepare the test environment before each test and clean up afterward, respectively. This is useful for setting up any necessary state or resources that your tests depend on.
# Additionally, you can organize your tests into test suites and run them together, which is helpful for larger projects with many tests. The unittest framework provides a TestLoader class that can help you discover and load tests automatically.
# Remember to write tests for both expected behavior and edge cases to ensure your code is robust and handles various scenarios correctly. Unit tests can also serve as documentation for your code, showing how functions are expected to behave under different conditions.
# You can also run the tests from the command line by using the following command:
# python -m unittest 038_unit_testing_with_unittest.py
# This will execute the tests defined in the file and provide a summary of the results.
# If you want to run a specific test method, you can specify it like this:
# python -m unittest 038_unit_testing_with_unittest.TestAddFunction.test_add_positive_numbers
# This will only run the specified test method, which is useful for debugging specific issues without running all tests.
# Unit testing is an essential practice in software development that helps ensure your code is functioning correctly and remains maintainable over time. By writing tests, you can catch bugs early, refactor code with confidence, and improve the overall quality of your software.
# In addition to the unittest framework, you can also explore other testing frameworks like pytest, which offers a more flexible and powerful approach to writing tests. Pytest allows for more concise test definitions, fixtures for setup and teardown, and better output formatting.
# Test fixtures:
# Fixtures are a way to provide a fixed baseline upon which tests can reliably and repeatedly execute. They can be used to set up any state or resources needed for the tests.
# In unittest, you can use the setUp() method to create fixtures that run before each test method. You can also use tearDown() to clean up after tests.
# Here's an example of using setUp() and tearDown() in the TestAddFunction class:
class TestAddFunctionWithFixtures(unittest.TestCase):
    """Test case for the add function with fixtures."""

    def setUp(self):
        """Set up test environment before each test."""
        self.a = 2
        self.b = 3

    def tearDown(self):
        """Clean up after each test."""
        pass  # No cleanup needed in this example

    def test_add_positive_numbers(self):
        """Test adding two positive numbers using fixtures."""
        self.assertEqual(add(self.a, self.b), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers using fixtures."""
        self.assertEqual(add(-self.a, -self.b), -5)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number using fixtures."""
        self.assertEqual(add(self.a, -self.b), -1)

    def test_add_zero(self):
        """Test adding zero to a number using fixtures."""
        self.assertEqual(add(0, self.b), 3)
        self.assertEqual(add(self.a, 0), 2)


if __name__ == "__main__":
    unittest.main()


# This example demonstrates how to use fixtures to set up common test data that can be reused across multiple test methods. The setUp() method initializes the values of `a` and `b`, which are then used in the test methods.
# The tearDown() method is included for completeness, but in this case, it doesn't perform any cleanup since there are no resources to release. You can use it to close files, release network connections, or perform other cleanup tasks as needed.
# Fixtures help keep your tests clean and focused by avoiding duplication of setup code in each test method. They also make it easier to maintain tests, as changes to the setup only need to be made in one place.
# You can also use class-level fixtures by defining setUpClass() and tearDownClass() methods. These methods run once for the entire test class, rather than before and after each individual test method. This is useful for expensive setup operations that don't need to be repeated for every test.
# Here's an example of using class-level fixtures:
class TestAddFunctionWithClassFixtures(unittest.TestCase):
    """Test case for the add function with class-level fixtures."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment once for the entire class."""
        cls.a = 2
        cls.b = 3

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests in the class."""
        pass  # No cleanup needed in this example

    def test_add_positive_numbers(self):
        """Test adding two positive numbers using class-level fixtures."""
        self.assertEqual(add(self.a, self.b), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers using class-level fixtures."""
        self.assertEqual(add(-self.a, -self.b), -5)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number using class-level fixtures."""
        self.assertEqual(add(self.a, -self.b), -1)

    def test_add_zero(self):
        """Test adding zero to a number using class-level fixtures."""
        self.assertEqual(add(0, self.b), 3)
        self.assertEqual(add(self.a, 0), 2)


if __name__ == "__main__":
    unittest.main()
# In this example, the setUpClass() method initializes the values of `a` and `b` once for the entire class, which can improve performance if the setup is expensive. The tearDownClass() method can be used to release any resources that were allocated during the setup.
# Class-level fixtures are particularly useful when you have multiple test methods that share the same setup, as they reduce redundancy and improve test performance. However, be cautious with class-level fixtures, as they can introduce state that may affect the tests if not managed carefully.
