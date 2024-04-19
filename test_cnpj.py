import pytest
from brutils.cnpj import sieve, remove_symbols, display, format_cnpj, validate, is_valid, generate, _hashdigit, _checksum

def test_sieve():
    assert sieve("12.345/6789-01") == "12345678901"
    assert sieve("98/76.543-2101") == "98765432101"

def test_remove_symbols():
    assert remove_symbols("12.345/6789-01") == "12345678901"
    assert remove_symbols("98/76.543-2101") == "98765432101"

def test_display():
    assert display("12345678901234") == "12.345.678/9012-34"
    assert display("98765432100100") == "98.765.432/1001-00"
    assert display("1234567890123") is None
    assert display("11111111111111") is None

def test_format_cnpj():
    assert format_cnpj("03560714000142") == '03.560.714/0001-42'
    assert format_cnpj("98765432100100") is None

def test_validate():
    assert validate("03560714000142") is True
    assert validate("00111222000133") is False

def test_is_valid():
    assert is_valid("03560714000142") is True
    assert is_valid("00111222000133") is False

def test_generate():
    cnpj = generate()
    assert is_valid(cnpj) is True

def test__hashdigit():
    assert _hashdigit("12345678901234", 13) == 3
    assert _hashdigit("98765432100100", 14) == 9

def test__checksum():
    assert _checksum("123456789012") == "30"
    assert _checksum("987654321001") == "41"