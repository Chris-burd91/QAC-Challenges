import pytest
from Programs import additionfunction

def test_addition_1():
    assert additionfunction.addition(9) == 11106

def test_addition_2():
   assert additionfunction.addition(2) == 2468

def test_addition_3():
   assert additionfunction.addition(5) == 6170

def test_addition_4():
   assert additionfunction.addition(14) == 14284256