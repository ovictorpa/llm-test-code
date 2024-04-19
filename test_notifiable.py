import pytest
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification

def test_notifiable_initialization():
    notifiable = Notifiable()
    assert notifiable.is_valid
    assert not notifiable.notifications

def test_notifiable_add_notification():
    notifiable = Notifiable()
    notification = Notification('key', 'message')
    notifiable.add_notification(notification)
    assert not notifiable.is_valid
    assert len(notifiable.notifications) == 1
    assert notifiable.notifications[0] == notification

def test_notifiable_add_notifications():
    notifiable = Notifiable()
    notifications = [Notification('key1', 'message1'), Notification('key2', 'message2')]
    notifiable.add_notifications(notifications)
    assert not notifiable.is_valid
    assert len(notifiable.notifications) == 2
    assert notifiable.notifications == notifications

def test_notifiable_get_notifications():
    notifiable = Notifiable()
    notifications = [Notification('key1', 'message1'), Notification('key2', 'message2')]
    notifiable.add_notifications(notifications)
    assert notifiable.get_notifications() == notifications

def test_notifiable_clear():
    notifiable = Notifiable()
    notifications = [Notification('key1', 'message1'), Notification('key2', 'message2')]
    notifiable.add_notifications(notifications)
    notifiable.clear()
    assert notifiable.is_valid
    assert not notifiable.notifications

def test_notifiable_get_notification_instance():
    notifiable = Notifiable()
    notification = notifiable.get_notification_instance('key', 'message')
    assert isinstance(notification, Notification)
    assert notification.key == 'key'
    assert notification.message == 'message'

def test_notifiable_str():
    notifiable = Notifiable()
    notifications = [Notification('key1', 'message1'), Notification('key2', 'message2')]
    notifiable.add_notifications(notifications)
    assert str(notifiable) == str(notifications)