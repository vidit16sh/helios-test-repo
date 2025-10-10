# helios-test-repo/test_app.py

import pytest
from unittest.mock import patch
from app import get_feature_status

def test_feature_status_when_off():
    """
    Tests the default behavior when the feature flag is OFF.
    This test should pass without any mocking.
    """
    assert get_feature_status() == "Feature is OFF"

@patch('app.FEATURE_FLAG_ENABLED', True)
def test_feature_status_when_on():
    """
    This test attempts to mock the feature flag to be ON.
    However, it uses the wrong path for the patch, so the mock will not work.
    This is the complex error that Helios should be able to diagnose.
    """
    # The developer expects the flag to be ON here, but it's still OFF.
    assert get_feature_status() == "Feature is ON"