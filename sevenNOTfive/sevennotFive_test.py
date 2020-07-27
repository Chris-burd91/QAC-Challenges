import pytest
from Programs import sevenNotFive

def test_1():
    assert sevenNotFive.seven_not_five(2000,3201)[0] == 2002

def test_2():
    assert sevenNotFive.seven_not_five(2000,3201)[6] == 2051

def test_3():
    assert sevenNotFive.seven_not_five(2000,3201)[6] % 7 == 0
    
def test_4():
    assert sevenNotFive.seven_not_five(2000,3201)[9] % 7 == 0

def test_5():
    assert sevenNotFive.seven_not_five(2000,3201)[6] % 5 != 0