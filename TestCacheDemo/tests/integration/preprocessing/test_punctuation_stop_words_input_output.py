import time
import unittest

from src.preprocessing.punctuation import remove_punctuation
from src.preprocessing.stop_words import remove_stop_words


class TestPunctuationStopWordsInputOutput(unittest.TestCase):

    def test_remove_punctuation(self):
        time.sleep(1)
        string = open("data/ThePhilosophersStone.txt").read()
        expected = open("data/ThePhilosophersStonePunctuationsStopWordsRemoved.txt").read()
        
        res = remove_punctuation(string)
        res = remove_stop_words(res)

        self.assertEqual(res, expected)

        
if __name__ == "__main__":
    unittest.main()
