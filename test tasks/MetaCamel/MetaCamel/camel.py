# -*- coding: utf-8 -*-

"""
to split text without spaces into list of words
https://stackoverflow.com/questions/38125281/split-sentence-without-space-in-python-nltk
Need install corpora/brown from nltk
>> import nltk
>> nltk.download('brown')
"""

from collections import Counter
import re, nltk

WORDS = nltk.corpus.brown.words()
COUNTS = Counter(WORDS)

def pdist(counter):
    "Make a probability distribution, given evidence from a Counter."
    N = sum(counter.values())
    return lambda x: counter[x]/N

P = pdist(COUNTS)

def Pwords(words):
    "Probability of words, assuming each word is independent of others."
    return product(P(w) for w in words)

def product(nums):
    "Multiply the numbers together.  (Like `sum`, but with multiplication.)"
    result = 1
    for x in nums:
        result *= x
    return result

def splits(text, start=0, L=20):
    "Return a list of all (first, rest) pairs; start <= len(first) <= L."
    return [(text[:i], text[i:])
            for i in range(start, min(len(text), L)+1)]

def segment(text):
    """Return a list of words that is the most probable segmentation of text.
    except for __  methods and attr"""
    if not text:
        return []
    elif text.startswith('_'):
        return [text]
    else:
        text = text.replace('_', '')
        text = text.lower()
        candidates = ([first] + segment(rest)
                      for (first, rest) in splits(text, 1))
        return max(candidates, key=Pwords)

def capel(lst):
    """Return CamelStyle name in lists
    https://stackoverflow.com/questions/2951701/is-it-possible-to-use-else-in-a-python-list-comprehension
    """
    lst_cap = [x.title() if not x.startswith('_') else x for x in lst]
    return ''.join(lst_cap)

def Camel(a):
    """Divide a compaund word into several simple words to list and split it capitalisated"""
    return capel(segment(a))


# print (segment('acquirecustomerdata'))
#['acquire', 'customer', 'data']
# print (segment('some_method'))
# print (segment('somemethod'))
# print (segment('somEmethod'))
# print (segment('_somemethod'))
# print (segment('makehabr'))
# print('---')
# print(Camel('somEmethod'))
# print(Camel('___somEmethod'))
