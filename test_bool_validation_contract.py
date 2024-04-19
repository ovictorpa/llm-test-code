import pytest
from flunt.validations.bool_validation_contract import BoolValidationContract



def test_is_false_with_false_value():
    contract = BoolValidationContract()
    contract.is_false(False, 'key', 'message')
    assert contract.is_valid

def test_is_false_with_true_value():
    contract = BoolValidationContract()
    contract.is_false(True, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_true_with_true_value():
    contract = BoolValidationContract()
    contract.is_true(True, 'key', 'message')
    assert contract.is_valid

def test_is_true_with_false_value():
    contract = BoolValidationContract()
    contract.is_true(False, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'
    
def test_is_false_with_none_value():
    contract = BoolValidationContract()
    contract.is_false(None, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_true_with_none_value():
    contract = BoolValidationContract()
    contract.is_true(None, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_false_with_non_boolean_value():
    contract = BoolValidationContract()
    contract.is_false('not a boolean', 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_true_with_non_boolean_value():
    contract = BoolValidationContract()
    contract.is_true('not a boolean', 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'