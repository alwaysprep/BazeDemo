import time
import unittest

from src.preprocessing.punctuation import remove_punctuation


class TestPunctuation(unittest.TestCase):

    def test_remove_punctuation(self):
        time.sleep(1)
        res = remove_punctuation("it. is! the: best;")
        self.assertEqual(res, "it is the best")

        
if __name__ == "__main__":
    unittest.main()
