import time
import unittest

from src.preprocessing.filter.filter import filter


class TestFiter(unittest.TestCase):

    def test_filter(self):
        time.sleep(1)
        res = filter("it. is! the: best;", ["es", "!"])
        self.assertEqual(res, "it. is the: bt;")

        
if __name__ == "__main__":
    unittest.main()
