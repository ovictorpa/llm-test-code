import pytest
from flunt.validations.collections_validation_contract import CollectionsValidationContract
from flunt.notifications.notification import Notification

def test_is_between_with_list_within_range():
    contract = CollectionsValidationContract()
    contract.is_between([1, 2, 3], 1, 3, 'key', 'message')
    assert contract.is_valid

def test_is_between_with_list_below_range():
    contract = CollectionsValidationContract()
    contract.is_between([1], 2, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_list_above_range():
    contract = CollectionsValidationContract()
    contract.is_between([1, 2, 3, 4], 1, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_string_within_range():
    contract = CollectionsValidationContract()
    contract.is_between('abc', 1, 3, 'key', 'message')
    assert contract.is_valid

def test_is_between_with_string_below_range():
    contract = CollectionsValidationContract()
    contract.is_between('a', 2, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_string_above_range():
    contract = CollectionsValidationContract()
    contract.is_between('abcd', 1, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_dict_within_range():
    contract = CollectionsValidationContract()
    contract.is_between({'a': 1, 'b': 2}, 1, 3, 'key', 'message')
    assert contract.is_valid

def test_is_between_with_dict_below_range():
    contract = CollectionsValidationContract()
    contract.is_between({'a': 1}, 2, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_dict_above_range():
    contract = CollectionsValidationContract()
    contract.is_between({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 1, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_set_within_range():
    contract = CollectionsValidationContract()
    contract.is_between({1, 2, 3}, 1, 3, 'key', 'message')
    assert contract.is_valid

def test_is_between_with_set_below_range():
    contract = CollectionsValidationContract()
    contract.is_between({1}, 2, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'

def test_is_between_with_set_above_range():
    contract = CollectionsValidationContract()
    contract.is_between({1, 2, 3, 4}, 1, 3, 'key', 'message')
    assert not contract.is_valid
    assert len(contract.get_notifications()) == 1
    assert contract.get_notifications()[0].message == 'message'