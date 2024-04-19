import pytest
from decimal import Decimal
from uuid import UUID
from collections import namedtuple
from typing import Iterable, Callable
from flunt.validations.commons_validation_contract import CommonsValidationContract
from flunt.notifications.notification import Notification

def test_is_none_with_none_value():
    contract = CommonsValidationContract()
    contract.is_none(None, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_none_with_string_value():
    contract = CommonsValidationContract()
    contract.is_none('string', 'key', 'message')
    assert contract.is_valid

def test_is_none_with_int_value():
    contract = CommonsValidationContract()
    contract.is_none(1, 'key', 'message')
    assert contract.is_valid

def test_is_none_with_list_value():
    contract = CommonsValidationContract()
    contract.is_none([1, 2, 3], 'key', 'message')
    assert contract.is_valid

def test_is_none_with_decimal_value():
    from decimal import Decimal
    contract = CommonsValidationContract()
    contract.is_none(Decimal('10.5'), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_float_value():
    contract = CommonsValidationContract()
    contract.is_none(1.23, 'key', 'message')
    assert contract.is_valid

def test_is_none_with_uuid_value():
    import uuid
    contract = CommonsValidationContract()
    contract.is_none(uuid.uuid4(), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_dict_value():
    contract = CommonsValidationContract()
    contract.is_none({'key': 'value'}, 'key', 'message')
    assert contract.is_valid

def test_is_none_with_object_value():
    class TestObject:
        pass
    contract = CommonsValidationContract()
    contract.is_none(TestObject(), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_set_value():
    contract = CommonsValidationContract()
    contract.is_none({1, 2, 3}, 'key', 'message')
    assert contract.is_valid

def test_is_none_with_struct_value():
    from collections import namedtuple
    TestStruct = namedtuple('TestStruct', 'field1 field2')
    contract = CommonsValidationContract()
    contract.is_none(TestStruct('value1', 'value2'), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_tuple_value():
    contract = CommonsValidationContract()
    contract.is_none((1, 2, 3), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_iterable_value():
    contract = CommonsValidationContract()
    contract.is_none(iter([1, 2, 3]), 'key', 'message')
    assert contract.is_valid

def test_is_none_with_callable_value():
    contract = CommonsValidationContract()
    contract.is_none(lambda: 'callable', 'key', 'message')
    assert contract.is_valid

def test_is_none_with_bool_value():
    contract = CommonsValidationContract()
    contract.is_none(True, 'key', 'message')
    assert contract.is_valid