def sort_str(string):
    """
    Accepts a string, sorts its characters, and returns the sorted string.
    """
    chars = list(string)
    chars.sort()
    result = ' '.join(chars)
    return result.replace(' ', '')

text = input()
print(sort_str(text))