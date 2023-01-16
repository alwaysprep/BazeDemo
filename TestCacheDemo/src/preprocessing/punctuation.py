from src.preprocessing.filter.filter import filter

def remove_punctuation(string):
    punctuations = {
        ".", ",", ":", "'", "”",
        "\"", ";", "“", "’",  "!"
    }
    
    return filter(string, punctuations)


# open("data/ThePhilosophersStonePunctuationsRemoved.txt", "w").write(remove_punctuation(open("data/ThePhilosophersStone.txt").read()))
