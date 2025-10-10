# helios-test-repo/test_app.py

from app import hello_world, process_order
import pytest
from unittest.mock import patch

def test_hello_world():
    assert hello_world() == "Hello, World!"

# New, complex test
def test_process_order_race_condition():
    """
    This test simulates a race condition where the database save
    is slower than the subsequent read.
    """
    # We patch 'get_from_db' to run BEFORE 'save_to_db' completes
    # by swapping the implementation for the test's purpose.
    with patch('app.save_to_db') as mock_save:
        # This is the key: we make the save function do nothing,
        # so the get function will fail.
        mock_save.side_effect = lambda order: None

        items = ["laptop", "mouse"]
        
        # This will raise a ValueError because the order was never saved.
        with pytest.raises(ValueError, match="Order 1 could not be confirmed"):
            process_order(items)