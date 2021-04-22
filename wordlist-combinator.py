#!/usr/bin/env python3
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='Combine a list of words in a list of combined words with separators')
parser.add_argument('-wc', '--word-count', type=int, help='How many words to combine together. Default is 3', nargs='?', default=3)
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
    for element in itertools.permutations(words, args.word_count):
        print(separator.join(element))
