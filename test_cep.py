import pytest
from brutils.cep import remove_symbols, format_cep, is_valid, generate

def test_remove_symbols():
    assert remove_symbols("123-45.678.9") == "123456789"
    assert remove_symbols("abc.xyz") == "abcxyz"

def test_format_cep():
    assert format_cep("12345678") == "12345-678"
    assert format_cep("12345") is None

def test_is_valid():
    assert is_valid("12345678") == True
    assert is_valid("12345") == False
    assert is_valid("abcdefgh") == False

def test_generate():
    cep = generate()
    assert len(cep) == 8
    assert cep.isdigit()