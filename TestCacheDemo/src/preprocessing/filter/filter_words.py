

def filter_words(string, filter_words, sep=None):
    return " ".join(
        word for word in string.split(sep) 
        if word.lower() not in filter_words
    )
