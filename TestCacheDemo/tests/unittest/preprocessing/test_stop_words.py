import time
import unittest

from src.preprocessing.stop_words import remove_stop_words


class TestStopWords(unittest.TestCase):

    def test_remove_stop_words(self):
        time.sleep(1)
        res = remove_stop_words("it is the best")
        self.assertEqual(res, "it best")

        
if __name__ == "__main__":
    unittest.main()
