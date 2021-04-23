#!/usr/bin/env python3
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='Combines a list of words in a list of combined words with separators')
parser.add_argument('-min', '--min-words', type=int, help='Minimum words to combine together. Default is 3', nargs='?', default=3)
parser.add_argument('-max', '--max-words', type=int, help='Maximum words to combine together. Default is 3', nargs='?', default=3)
parser.add_argument('-s', '--separators', metavar='N', type=str, nargs='?', help='Separators between combined words. Default is \"-_\". Empty separator is always included.', default=["-","_"])
parser.add_argument('-o', '--output-file', type=str, help='Outputs to a file in addition to stdout', nargs='?')
parser.add_argument('file')
args = parser.parse_args()


# Open dictionary file
words = []
try:
    with open(args.file) as fp:
        for line in fp:
            words.append(line.rstrip())
except FileNotFoundError as not_found:
    print("Error: File " + not_found.filename + " not found")
    quit()

# Open output file if required
if args.output_file is not None:
    try:
        f = open(args.output_file, 'w')
    except:
        print("Error opening output file")
        quit()

separators = [char for char in args.separators]
separators.append("")

for separator in separators:
    for words_count in range(args.min_words, args.max_words + 1):
        for element in itertools.permutations(words, words_count):
            candidate = separator.join(element)
            print(candidate)
            # Print to output file if required
            if args.output_file is not None:
                f.write(candidate + "\n")


if args.output_file is not None:
    f.close()
