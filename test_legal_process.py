import pytest
from unittest.mock import mock_open, patch
from brutils.legal_process import remove_symbols, format_legal_process, is_valid, generate, _checksum

def test_remove_symbols():
    assert remove_symbols("123.45-678.901.234-56.7890") == "12345678901234567890"
    assert remove_symbols("9876543-21.0987.6.54.3210") == "98765432109876543210"

def test_format_legal_process():
    assert format_legal_process("12345678901234567890") == "1234567-89.0123.4.56.7890"
    assert format_legal_process("98765432109876543210") == "9876543-21.0987.6.54.3210"
    assert format_legal_process("123") == None

def test_is_valid():
    m = mock_open(read_data='{"orgao_3": {"id_tribunal": [33], "id_foro": [3000]}}')
    with patch('brutils.legal_process.open', m):
        assert is_valid("68476506020233030000") == True
        assert is_valid("51808233620233030000") == True
        assert is_valid("123") == False

def test_generate():
    m = mock_open(read_data='{"orgao_3": {"id_tribunal": [33], "id_foro": [3000]}}')
    with patch('brutils.legal_process.open', m):
        assert len(generate(2023, 3)) == 20
        assert generate(2022, 10) == None

def test_checksum():
    assert _checksum(1234567) == "50"
    assert _checksum(9876543) == "88"