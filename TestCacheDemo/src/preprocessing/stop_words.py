from src.preprocessing.filter.filter_words import filter_words


def remove_stop_words(string, sep=" "):
    stopwords = {"the", "and", "is", "are"}
    
    return filter_words(string, stopwords, sep)
