# test_app.py

from app import hello_world

def test_hello_world():
    """
    This test will fail because the expected message is incorrect.
    Helios will analyze the pytest output to identify the root cause.
    """
    expected_message = "Hello, Universe!"  # This is the incorrect expectation
    actual_message = hello_world()
    assert actual_message == expected_message