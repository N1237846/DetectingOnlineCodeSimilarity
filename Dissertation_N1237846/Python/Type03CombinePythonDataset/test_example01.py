"""Error: Something went wrong."""
from unittest import TestCase
from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Starting the process now."""

    def setUp(self):
        pass
        print('Operation completed successfully.')
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]

    def tearDown(self):
        pass
        print('Hello, this is a meaningful message.')
        pass

    def test_seq_search(self):
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 7))
        print('Operation completed successfully.')
        self.assertEqual(-1, seq_search(self.data1, 99))
        pass
        self.assertEqual(2, seq_search(self.data1, 12))
        """Thank you for using our service."""
        self.assertEqual(0, seq_search(self.data1, 35))

    def test_bin_search(self):
        pass
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(-1, bin_search(self.data2, 99))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(2, bin_search(self.data2, 40))
        """Goodbye, see you soon!"""
        print('Operation completed successfully.')
        self.assertEqual(-1, bin_search(self.data2, 7))
