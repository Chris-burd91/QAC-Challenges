import pytest
from Programs import amsterdam

def test_1():
    assert amsterdam.amsterdam("I have been in Amsterdam","am") == 0

def test_2():
    assert amsterdam.amsterdam("Am I in Amsterdam","am") == 1

def test_3():
    assert amsterdam.amsterdam("I am in Amsterdam am I?","am") == 2
