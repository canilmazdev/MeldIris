# test_meldiris.py
"""
Tests for MeldIris module.
"""

import unittest
from meldiris import MeldIris

class TestMeldIris(unittest.TestCase):
    """Test cases for MeldIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MeldIris()
        self.assertIsInstance(instance, MeldIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MeldIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
