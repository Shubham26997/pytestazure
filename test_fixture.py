import pytest
@pytest.fixture
def my_function(n):
    n += 5
    return [n,15]

def testfile1_method2(my_function):
	
	assert my_function[0] == 6,"X and Y are not equal"
