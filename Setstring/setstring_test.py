import pytest
from Programs import setstring

def test_setstring_1():
    assert setstring.setstring("hello again") == "again hello" 

def test_setstring_2():
    assert setstring.setstring("tango zedbra basketball") == "basketball tango zedbra"

def test_setstring_3():
    assert setstring.setstring("challenge of the day") == "challenge day of the"

def test_setstring_4():
    assert setstring.setstring("hello hello") == "hello"
