

def filter(string, filter_items):
    for item in filter_items:
        string = string.replace(item, "")
    return string
