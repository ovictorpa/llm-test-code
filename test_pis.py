import pytest
from brutils.pis import (
    format_pis,
    is_valid,
    remove_symbols,
    generate,
    _checksum,

)

def test_remove_symbols():
    assert remove_symbols("123.456.789-09") == "12345678909"
    assert remove_symbols("98765432100") == "98765432100"
    assert remove_symbols("123-456.789.09") == "12345678909"
    assert remove_symbols("...---...") == ""

def test_format_pis():
    assert format_pis("12345678909") == "123.45678.90-9"
    assert format_pis("98765432100") == "987.65432.10-0"
    assert format_pis("1234567890") is None
    assert format_pis("123456789ab") is None

def test_is_valid():
    assert is_valid("82178537464") is True
    assert is_valid("55550207753") is True
    assert is_valid("1234567890") is False
    assert is_valid("123456789ab") is False
    assert is_valid(12345678909) is False

def test_generate():
    for _ in range(100):
        pis = generate()
        assert len(pis) == 11
        assert pis.isdigit()
        assert is_valid(pis)

def test_checksum():
    assert _checksum("1234567890") == 9
    assert _checksum("9876543210") == 0
    assert _checksum("1111111111") == 1
    assert _checksum("0000000000") == 0