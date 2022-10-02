import collections

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i, item in enumerate(items):
        items[i] = str(item)
    frequencies = dict(collections.Counter(items))
    # Your code goes here
    return frequencies