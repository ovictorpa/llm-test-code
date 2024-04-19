import pytest
from brutils.license_plate import (
    convert_to_mercosul,
    format_license_plate,
    is_valid,
    remove_symbols,
    get_format,
    generate,
    _is_valid_old_format,
    _is_valid_mercosul,
)

def test_remove_symbols():
    assert remove_symbols("ABC-123") == "ABC123"
    assert remove_symbols("abc123") == "abc123"
    assert remove_symbols("ABCD123") == "ABCD123"

def test_convert_to_mercosul():
    assert convert_to_mercosul("AAA1011") == "AAA1A11"
    assert convert_to_mercosul("AAA1111") == "AAA1B11"
    assert convert_to_mercosul("AAA1211") == "AAA1C11"
    assert convert_to_mercosul("AAA1311") == "AAA1D11"
    assert convert_to_mercosul("AAA1411") == "AAA1E11"
    assert convert_to_mercosul("AAA1511") == "AAA1F11"
    assert convert_to_mercosul("AAA1611") == "AAA1G11"
    assert convert_to_mercosul("AAA1711") == "AAA1H11"
    assert convert_to_mercosul("AAA1811") == "AAA1I11"
    assert convert_to_mercosul("AAA1911") == "AAA1J11"
    assert convert_to_mercosul("abc1234") == "ABC1C34"

def test_format_license_plate():
    assert format_license_plate("ABC1234") == "ABC-1234"
    assert format_license_plate("abc1234") == "ABC-1234"
    assert format_license_plate("ABC1D23") == "ABC1D23"
    assert format_license_plate("abc1d23") == "ABC1D23"

def test_get_format():
    assert get_format("ABC1234") == "LLLNNNN"
    assert get_format("abc1234") == "LLLNNNN"
    assert get_format("ABC4E67") == "LLLNLNN"
    assert get_format("XXX9X99") == "LLLNLNN"

def test_is_valid():
    assert is_valid("ABC1234", "old_format") == True
    assert is_valid("ABC4E67", "mercosul") == True
    assert is_valid("ABC1234") == True
    assert is_valid("ABC4E67") == True

def test_generate():
    assert _is_valid_mercosul(generate(format="LLLNLNN")) == True
    assert _is_valid_old_format(generate(format="LLLNNNN")) == True
    assert _is_valid_mercosul(generate()) == True
    assert generate("LNLNLNL") == None