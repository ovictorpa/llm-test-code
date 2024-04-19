import pytest
from brutils.phone import (
    format_phone,
    is_valid,
    remove_symbols_phone,
    generate,
    remove_international_dialing_code,
)

# Test for format_phone function
def test_format_phone():
    assert format_phone("11994029275") == "(11)99402-9275"
    assert format_phone("1635014415") == "(16)3501-4415"
    assert format_phone("333333") is None

# Test for is_valid function
def test_is_valid():
    assert is_valid("11994029275") == True
    assert is_valid("1635014415") == True
    assert is_valid("333333") == False

# Test for remove_symbols_phone function
def test_remove_symbols_phone():
    assert remove_symbols_phone("(11)99402-9275") == "11994029275"
    assert remove_symbols_phone("+55 16 3501-4415") == "551635014415"
    assert remove_symbols_phone("333-333") == "333333"

# Test for generate function
def test_generate():
    assert len(generate("mobile")) == 11
    assert len(generate("landline")) == 10
    assert len(generate()) in [10, 11]

# Test for remove_international_dialing_code function
def test_remove_international_dialing_code():
    assert remove_international_dialing_code("5511994029275") == "11994029275"
    assert remove_international_dialing_code("1635014415") == "1635014415"
    assert remove_international_dialing_code("+5511994029275") == "+11994029275"