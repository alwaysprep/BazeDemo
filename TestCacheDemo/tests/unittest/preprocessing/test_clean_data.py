import time
import unittest

from src.preprocessing.clean_data import remove_stop_words


class TestCleanData(unittest.TestCase):

    def test_remove_stop_words(self):
        time.sleep(2)
        res = remove_stop_words("it is the best")
        self.assertEqual(res, "it best")

        
if __name__ == "__main__":
    unittest.main()
