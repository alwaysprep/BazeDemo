

def remove_stop_words(string):
    stopwords = {"the", "and", "is", "are", "not"}
    
    return " ".join(
        word for word in string.split() 
        if word.lower() not in stopwords
    )

