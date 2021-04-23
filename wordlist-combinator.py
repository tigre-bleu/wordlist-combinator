#!/usr/bin/env python3
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='Combine a list of words in a list of combined words with separators')
parser.add_argument('-min', '--min-words', type=int, help='Minimum words to combine together. Default is 3', nargs='?', default=3)
parser.add_argument('-max', '--max-words', type=int, help='Maximum words to combine together. Default is 3', nargs='?', default=3)
parser.add_argument('-s', '--separators', metavar='N', type=str, nargs='?', help='Separators between combined words. Default is \"-_\". Empty separator is always included.', default=["-","_"])
parser.add_argument('file')
args = parser.parse_args()

words = []
try:
    with open(args.file) as fp:
        for line in fp:
            words.append(line.rstrip())
except FileNotFoundError as not_found:
    print("Error: File " + not_found.filename + " not found")
    quit()

separators = [char for char in args.separators]
separators.append("")

for separator in separators:
    for words_count in range(args.min_words, args.max_words + 1):
        for element in itertools.permutations(words, words_count):
            print(separator.join(element))
