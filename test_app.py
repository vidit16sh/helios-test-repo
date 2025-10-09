# test_app.py

from app import hello_world
import pytest

def test_hello_world():
    """
    This test will fail because the expected message is incorrect.
    Helios will analyze the pytest output to identify the root cause.
    """
    expected_message = "Hello, Universe!"  # This is the incorrect expectation
    actual_message = hello_world()
    assert actual_message == expected_message

def test_hello_world_is_not_goodbye():
    """A new failing test to check for a different string."""
    actual_message = hello_world()
    assert actual_message == "Goodbye, World!"

def test_hello_world_type():
    """A new failing test to check the return type."""
    actual_message = hello_world()
    assert isinstance(actual_message, int)