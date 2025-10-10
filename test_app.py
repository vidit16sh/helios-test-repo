# helios-test-repo/test_app.py

import pytest
from unittest.mock import patch
from app import get_feature_status

def test_feature_status_when_off():
    """
    Tests the default behavior when the feature flag is OFF.
    This test should pass.
    """
    assert get_feature_status() == "Feature is OFF"

# THIS IS THE CORRECTED, FAILING TEST
@patch('config.FEATURE_FLAG_ENABLED', True)
def test_feature_status_when_on_with_bad_mock():
    """
    This test attempts to mock the feature flag where it is DEFINED,
    not where it is USED. This is a common mistake and will cause the
    test to fail, which is what we want.
    """
    # The developer expects the flag to be ON here, but the mock
    # didn't work, so the function will still return "Feature is OFF".
    assert get_feature_status() == "Feature is ON"