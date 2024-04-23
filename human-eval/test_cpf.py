import pytest
from brutils.cpf import sieve, remove_symbols, display, format_cpf, validate, is_valid, generate, _hashdigit, _checksum

def test_sieve():
    assert sieve("123.456.789-01") == "12345678901"
    assert sieve("987-654-321.01") == "98765432101"

def test_remove_symbols():
    assert remove_symbols("123.456.789-01") == "12345678901"
    assert remove_symbols("987-654-321.01") == "98765432101"

def test_display():
    assert display("12345678901") == "123.456.789-01"
    assert display("98765432101") == "987.654.321-01"
    assert display("1234567890a") == None
    assert display("123456789") == None

def test_format_cpf():
    assert format_cpf("82178537464") == '821.785.374-64'
    assert format_cpf("55550207753") == '555.502.077-53'
    assert format_cpf("12345678901") == None

def test_validate():
    assert validate("82178537464") == True
    assert validate("55550207753") == True
    assert validate("12345678901") == False

def test_is_valid():
    assert is_valid("82178537464") == True
    assert is_valid("55550207753") == True
    assert is_valid("12345678901") == False

def test_generate():
    for _ in range(100):
        cpf = generate()
        assert is_valid(cpf) == True

def test__hashdigit():
    assert _hashdigit("52599927765", 11) == 5
    assert _hashdigit("52599927765", 10) == 6

def test__checksum():
    assert _checksum("335451269") == '51'
    assert _checksum("382916331") == '26'