# test_metalab.py
"""
Tests for MetaLab module.
"""

import unittest
from metalab import MetaLab

class TestMetaLab(unittest.TestCase):
    """Test cases for MetaLab class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaLab()
        self.assertIsInstance(instance, MetaLab)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaLab()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
