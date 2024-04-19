import pytest
from flunt.validations.strings_validation_contract import Contract, Notification

class TestContract:
    
    def test_not_contains_with_matching_string(self):
        """Test if not_contains adds a notification when the comparer is found in the value."""
        obj = Contract().not_contains("Hello", "World", "Comparison", "Value should not contain 'World'")
        assert len(obj.notifications) == 1
        assert isinstance(obj.notifications[0], Notification)
        assert obj.notifications[0].key == "Comparison"
        assert obj.notifications[0].message == "Value should not contain 'World'"

    def test_not_contains_with_non_matching_string(self):
        """Test if not_contains does not add a notification when the comparer is not found in the value."""
        obj = Contract().not_contains("Hello", "Foo", "Comparison", "Value should not contain 'Foo'")
        assert len(obj.notifications) == 0

    def test_not_contains_with_empty_string(self):
        """Test if not_contains does not add a notification when the comparer is an empty string."""
        obj = Contract().not_contains("Hello", "", "Comparison", "Value should not contain ''")
        assert len(obj.notifications) == 0

    def test_not_contains_with_none_comparer(self):
        """Test if not_contains does not add a notification when the comparer is None."""
        obj = Contract().not_contains("Hello", None, "Comparison", "Value should not contain None")
        assert len(obj.notifications) == 0

    def test_not_contains_with_none_value(self):
        """Test if not_contains adds a notification when the value is None."""
        obj = Contract().not_contains(None, "World", "Comparison", "Value should not contain 'World'")
        assert len(obj.notifications) == 1
        assert isinstance(obj.notifications[0], Notification)
        assert obj.notifications[0].key == "Comparison"
        assert obj.notifications[0].message == "Value should not contain 'World'"

    def test_contains_with_matching_string(self):
        """Test if contains adds a notification when the comparer is found in the value."""
        obj = Contract().contains("Hello World", "World", "Comparison", "Value should contain 'World'")
        assert len(obj.notifications) == 1
        assert isinstance(obj.notifications[0], Notification)
        assert obj.notifications[0].key == "Comparison"
        assert obj.notifications[0].message == "Value should contain 'World'"

    def test_contains_with_non_matching_string(self):
        """Test if contains does not add a notification when the comparer is not found in the value."""
        obj = Contract().contains("Hello World", "Foo", "Comparison", "Value should contain 'Foo'")
        assert len(obj.notifications) == 0

    def test_contains_with_empty_string(self):
        """Test if contains adds a notification when the comparer is an empty string."""
        obj = Contract().contains("Hello World", "", "Comparison", "Value should contain ''")
        assert len(obj.notifications) == 1
        assert isinstance(obj.notifications[0], Notification)
        assert obj.notifications[0].key == "Comparison"
        assert obj.notifications[0].message == "Value should contain ''"

    def test_contains_with_none_comparer(self):
        """Test if contains does not add a notification when the comparer is None."""
        obj = Contract().contains("Hello World", None, "Comparison", "Value should contain None")
        assert len(obj.notifications) == 0

    def test_contains_with_none_value(self):
        """Test if contains adds a notification when the value is None."""
        obj = Contract().contains(None, "World", "Comparison", "Value should contain 'World'")
        assert len(obj.notifications) == 1
        assert isinstance(obj.notifications[0], Notification)
        assert obj.notifications[0].key == "Comparison"
        assert obj.notifications[0].message == "Value should contain 'World'"