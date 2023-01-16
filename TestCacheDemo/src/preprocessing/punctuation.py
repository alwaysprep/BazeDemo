from src.preprocessing.filter.filter import filter

def remove_punctuation(string):
    punctuations = {
        ".", ",", ":", "'", "”",
        "\"", ";", "“", "’",  "!"
    }
    
    return filter(string, punctuations)
