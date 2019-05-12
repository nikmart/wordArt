"""
findWords.py

Purpose: Find words when you decompose a word into two seperate words.

Usage: findwords.py [dictonary.txt]

Dictionary source: http://gwicks.net/dictionaries.htm
Dictionary text encoding: ISO-8859-1
"""

import argparse
import math

parser = argparse.ArgumentParser(description='Find words in words.')
parser.add_argument('--dict', help="dictonary file")
parser.add_argument('--len', help="minimum word length")

args = parser.parse_args()
MIN_WORD_LEN = int(args.len)


# Put the dictionary in a python dictionary so that we can search it with O(1)
d = {}
with open(args.dict, encoding="ISO-8859-1") as f:
    for line in f:
        if "'s" in line:
            pass
        else:
            key = line.strip()
            d[key] = 1

# Break down each word into two words and see if they are each words
for word in d.keys():
    word1 = []
    word2 = []
    for n,letter in enumerate(word):
        if int(math.fmod(n,2)): # even
            word2.append(letter)
        else: # odd
            word1.append(letter)
    word1 = ''.join(word1)
    word2 = ''.join(word2)
    # check if the first word is 2+ letters in the dict
    if (len(word1) >= MIN_WORD_LEN) and (word1 in d):
        # check if word2 is in the dict
        if (len(word2) >= MIN_WORD_LEN) and (word2 in d):
            print(word, word1, word2)

