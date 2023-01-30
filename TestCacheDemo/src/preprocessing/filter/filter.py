

def filter(string, filter_items: list):
    for item in filter_items:
        string = string.replace(item, "")
    return string
