import time
import unittest

from src.preprocessing.stop_words import remove_stop_words


class TestStopWordsInput(unittest.TestCase):

    def test_remove_stop_words(self):
        time.sleep(1)
        string = open("data/ThePhilosophersStone.txt").read()

        self.assertEqual(len(string), 474428)
        
        res = remove_stop_words(string)
        self.assertEqual(len(res), 451047)

        
if __name__ == "__main__":
    unittest.main()
