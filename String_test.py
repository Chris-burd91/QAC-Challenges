import pytest
import String_gen


def test_str_type():
    assert type(String_gen.str_gen()) == str #Checks if the functions return is a string datatype

def test_str_len():
    assert len(String_gen.str_gen()) == 5  #Checks if the length of the functions string is 5 characters long

def test_str_lowercase():
    assert str.islower(String_gen.str_gen()) == True #Checks if the string is all lowercase