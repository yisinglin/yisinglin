"""
This module contains test cases for the hello module.
"""

from hello import toyou, add, subtract

class TestHello:
    def setup_method(self, method):
        """
        Setup method to initialize test conditions.
        
        Args:
        method (method): The test method.
        """
        print(f" Running Setup: {method.__name__}")
        self.x = 10

    def teardown_method(self, method):
        """
        Teardown method to clean up after tests.
        
        Args:
        method (method): The test method.
        """
        print(f" Running Teardown: {method.__name__}")
        del self.x

    def test_hello_toyou(self):
        """
        Test case for toyou function.
        """
        assert toyou("test") == "hi test", "Failed test_hello_toyou"

    def test_hello_add(self):
        """
        Test case for add function.
        """
        assert add(self.x) == 11, "Failed test_hello_add"

    def test_hello_subtract(self):
        """
        Test case for subtract function.
        """
        assert subtract(self.x) == 9, "Failed test_hello_subtract"

# Note: No need to explicitly call test functions; a test runner like pytest will handle this.
