import pytest
from brutils.email import is_valid

def test_valid_email():
    valid_emails = [
        "joao.ninguem@gmail.com",
        "user123@gmail.com",
        "test.email@mydomain.co.uk",
        "johndoe@sub.domain.example",
        "f99999999@place.university-campus.ac.in",
    ]
    for email in valid_emails:
        assert is_valid(email), f"Expected True for email: {email}"

def test_invalid_email():
    invalid_emails = [
        ".joao.ninguem@gmail.com",
        "joao ninguem@gmail.com",
        "not_an_email",
        "@missing_username.com",
        "user@incomplete.",
        "user@.incomplete",
        "user@inva!id.com",
        "user@missing-tld.",
    ]
    for email in invalid_emails:
        assert not is_valid(email), f"Expected False for email: {email}"

def test_non_string_input():
    non_strings = [None, 123, True, ["test@example.com"]]
    for value in non_strings:
        assert not is_valid(value), f"Expected False for non-string value: {value}"

def test_empty_string():
    assert not is_valid(""), "Expected False for empty string"