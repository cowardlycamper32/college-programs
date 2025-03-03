import pytest as pt


# to write tests first import the script and set it to target:
from unitTesting.intentionallybadprogram import sum

# define a class for the test:
class TestSum:
    # define a function for the individual test
    def test_list_int(self):
        """
        test it can sum of a list of integers
        """
        data = [1, 2, 3]
        result = sum(data[0], data[1], data[2])
        # assert with test value and message
        assert result == 7, "should be 7"

