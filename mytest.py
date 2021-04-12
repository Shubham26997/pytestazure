import pytest
# @pytest.fixture
def my_function(n):
    n += 5
    return [n,15]

a = my_function(3)
print(a)



