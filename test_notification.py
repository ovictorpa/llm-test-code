import pytest
from flunt.notifications.notification import Notification

def test_notification_initialization():
    notification = Notification('field', 'message')
    assert notification.field == 'field'
    assert notification.message == 'message'

def test_notification_str():
    notification = Notification('field', 'message')
    assert str(notification) == '{field: field, message: message}'

# Test with different field and message
def test_notification_initialization_different_field_message():
    notification = Notification('different_field', 'different_message')
    assert notification.field == 'different_field'
    assert notification.message == 'different_message'

def test_notification_str_different_field_message():
    notification = Notification('different_field', 'different_message')
    assert str(notification) == '{field: different_field, message: different_message}'

# Test with empty field and message
def test_notification_initialization_empty_field_message():
    notification = Notification('', '')
    assert notification.field == ''
    assert notification.message == ''

def test_notification_str_empty_field_message():
    notification = Notification('', '')
    assert str(notification) == '{field: , message: }'