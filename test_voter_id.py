import pytest
from brutils.voter_id import is_valid

def test_is_valid_with_valid_voter_id():
    assert is_valid("217633460930") == True

def test_is_valid_with_invalid_voter_id():
    assert is_valid("123456789011") == False

def test_is_valid_with_invalid_length():
    assert is_valid("12345678901") == False
    assert is_valid("1234567890123") == False

def test_is_valid_with_invalid_characters():
    assert is_valid("ABCD56789012") == False
    assert is_valid("217633 460 930") == False

def test_is_valid_with_valid_special_case():
    assert is_valid("3244567800167") == True

def test_is_valid_with_invalid_vd1():
    assert is_valid("427503840223") == False

def test_is_valid_with_invalid_vd2():
    assert is_valid("427503840214") == False