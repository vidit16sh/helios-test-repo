# helios-test-repo/test_app.py

from app import hello_world, process_order
import pytest
from unittest.mock import patch

def test_hello_world():
    assert hello_world() == "Hello, World!"

# This is the corrected, failing test
def test_process_order_fails_without_save():
    """
    This test simulates a race condition by preventing the database save.
    The unhandled ValueError will now cause the pytest run to fail.
    """
    with patch('app.save_to_db') as mock_save:
        # This mock prevents the order from being saved to the DB
        mock_save.side_effect = lambda order: None
        
        items = ["laptop", "mouse"]
        
        # We call the function directly. When it raises the ValueError,
        # pytest will catch it and mark the entire test run as FAILED
        # because the error was not expected to be handled.
        process_order(items)