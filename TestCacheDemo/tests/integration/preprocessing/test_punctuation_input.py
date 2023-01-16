import time
import unittest

from src.preprocessing.punctuation import remove_punctuation


class TestPunctuationInput(unittest.TestCase):

    def test_remove_punctuation(self):
        time.sleep(1)
        string = open("data/ThePhilosophersStone.txt").read()

        self.assertEqual(len(string), 474428)
        
        res = remove_punctuation(string)
        self.assertEqual(len(res), 453297)

        
if __name__ == "__main__":
    unittest.main()
