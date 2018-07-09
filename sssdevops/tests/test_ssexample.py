"""
Unit and regression test for the myexample package.
"""

# Import package, test suite, and other packages as needed
import myexample
import pytest
import sys

def test_myexample_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "myexample" in sys.modules
