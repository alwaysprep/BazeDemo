

def remove_stop_words(string, sep=" "):
    stopwords = {"the", "and", "is", "are"}
    
    return " ".join(
        word for word in string.split(sep) 
        if word.lower() not in stopwords
    )


# open("data/ThePhilosophersStoneStopWordsRemoved.txt", "w").write(remove_stop_words(open("data/ThePhilosophersStone.txt").read()))
