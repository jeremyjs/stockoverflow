# returns one key which maps to the maximum value in dict.values()
def max_key(dict):
    values = list(dict.values())
    keys = list(dict.keys())
    return keys[values.index(max(values))]
