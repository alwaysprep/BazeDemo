import time
import unittest

from src.preprocessing.clean_data import remove_stop_words


class TestCleanData(unittest.TestCase):

    def test_remove_stop_words(self):
        time.sleep(2)
        string = open("data/ThePhilosophersStone.txt").read()

        self.assertEqual(len(string), 474429)
        
        res = remove_stop_words(string)
        self.assertEqual(len(res), 433640)

        
if __name__ == "__main__":
    unittest.main()
