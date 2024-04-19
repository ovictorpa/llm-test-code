import pytest
from collections import namedtuple
from flunt.validations.contract import Contract
from flunt.notifications.notification import Notification

def test_requires_with_empty_string():
    contract = Contract()
    contract.requires('', 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_requires_with_non_empty_string():
    contract = Contract()
    contract.requires('non-empty string', 'key', 'message')
    assert contract.is_valid

def test_requires_with_empty_list():
    contract = Contract()
    contract.requires([], 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_requires_with_non_empty_list():
    contract = Contract()
    contract.requires([1, 2, 3], 'key', 'message')
    assert contract.is_valid

def test_requires_with_empty_dict():
    contract = Contract()
    contract.requires({}, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_requires_with_non_empty_dict():
    contract = Contract()
    contract.requires({'key': 'value'}, 'key', 'message')
    assert contract.is_valid

def test_requires_with_none_value():
    contract = Contract()
    contract.requires(None, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_requires_with_true_value():
    contract = Contract()
    contract.requires(True, 'key', 'message')
    assert contract.is_valid

def test_requires_with_false_value():
    contract = Contract()
    contract.requires(False, 'key', 'message')
    assert contract.is_valid

def test_requires_with_zero_value():
    contract = Contract()
    contract.requires(0, 'key', 'message')
    assert contract.is_valid

def test_requires_with_positive_int_value():
    contract = Contract()
    contract.requires(1, 'key', 'message')
    assert contract.is_valid

def test_requires_with_negative_int_value():
    contract = Contract()
    contract.requires(-1, 'key', 'message')
    assert contract.is_valid

def test_requires_with_positive_float_value():
    contract = Contract()
    contract.requires(1.23, 'key', 'message')
    assert contract.is_valid

def test_requires_with_negative_float_value():
    contract = Contract()
    contract.requires(-1.23, 'key', 'message')
    assert contract.is_valid

def test_requires_with_struct_value():
    from collections import namedtuple
    TestStruct = namedtuple('TestStruct', 'field1 field2')
    contract = Contract()
    contract.requires(TestStruct('value1', 'value2'), 'key', 'message')
    assert contract.is_valid

def test_requires_with_tuple_value():
    contract = Contract()
    contract.requires((1, 2, 3), 'key', 'message')
    assert contract.is_valid

def test_requires_with_iterable_value():
    contract = Contract()
    contract.requires(iter([1, 2, 3]), 'key', 'message')
    assert contract.is_valid

def test_requires_with_callable_value():
    contract = Contract()
    contract.requires(lambda: 'callable', 'key', 'message')
    assert contract.is_valid