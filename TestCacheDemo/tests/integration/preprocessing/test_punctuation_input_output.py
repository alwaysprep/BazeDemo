import time
import unittest

from src.preprocessing.punctuation import remove_punctuation


class TestPunctuationInputOutput(unittest.TestCase):

    def test_remove_punctuation(self):
        time.sleep(1)
        string = open("data/ThePhilosophersStone.txt").read()
        expected = open("data/ThePhilosophersStonePunctuationsRemoved.txt").read()
        
        res = remove_punctuation(string)

        self.assertEqual(res, expected)

        
if __name__ == "__main__":
    unittest.main()
