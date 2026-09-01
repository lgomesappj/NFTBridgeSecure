# test_nftbridgesecure.py
"""
Tests for NFTBridgeSecure module.
"""

import unittest
from nftbridgesecure import NFTBridgeSecure

class TestNFTBridgeSecure(unittest.TestCase):
    """Test cases for NFTBridgeSecure class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTBridgeSecure()
        self.assertIsInstance(instance, NFTBridgeSecure)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTBridgeSecure()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
