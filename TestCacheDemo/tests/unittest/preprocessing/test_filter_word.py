import time
import unittest

from src.preprocessing.filter.filter_words import filter_words


class TestFiterWords(unittest.TestCase):

    def test_filter_words(self):
        time.sleep(1)
        res = filter_words("it. is the best;", ["the", "is"])
        self.assertEqual(res, "it. best;")

        
if __name__ == "__main__":
    unittest.main()
