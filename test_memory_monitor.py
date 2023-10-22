import unittest
from unittest.mock import patch
from memory_monitor import check_memory_usage


class TestMemoryUsage(unittest.TestCase):
    def test_memory_above_threshold(self):
        with patch("psutil.virtual_memory") as mock_vm:
            mock_vm.return_value.percent = 85
            self.assertTrue(check_memory_usage())

    def test_memory_below_threshold(self):
        with patch("psutil.virtual_memory") as mock_vm:
            mock_vm.return_value.percent = 70
            self.assertFalse(check_memory_usage())


if __name__ == "__main__":
    unittest.main()
