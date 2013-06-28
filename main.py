from collections import Counter
from itertools import islice
import re


def get_totals(words):
    # case insensitive search
    return Counter(re.findall('\w+', words.lower()))


def take(n, iter):
    # take first n items from an iterable
    return list(islice(iter, n))


def main(n):
    # read words
    with open('sample.txt') as f:
        words = f.read()
    counted_words = get_totals(words)
    # sort by value desc
    sorted_words = list(sorted(counted_words, key=counted_words.__getitem__, reverse=True))

    return take(n, sorted_words)

if __name__ == '__main__':
    print main(15)