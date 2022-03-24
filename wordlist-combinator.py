#!/usr/bin/env python3
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='Combines a list of words in a list of combined words with separators. \
        Example: wordlist-combinator.py -min 2 -max 4 -s \"_-.\" -o merged.lst example.lst')
parser.add_argument('-min', '--min-words', type=int, help='Minimum words to combine together (if single file is provided). Default is 3', nargs='?', default=3)
parser.add_argument('-max', '--max-words', type=int, help='Maximum words to combine together (if single file is provided). Default is 3', nargs='?', default=3)
parser.add_argument('-s', '--separators', metavar='N', type=str, nargs='?', help='Separators between combined words. Default is \"-_\". Empty separator is always included. Example: \"_-.,\"', default=["-","_"])
parser.add_argument('-o', '--output-file', type=str, help='Outputs to a file in addition to stdout', nargs='?')
parser.add_argument('files', help='if single argument: combine all lines, if multiple arguments: combine lines from all files', nargs='+')
args = parser.parse_args()

if len(args.files) == 1:
    if args.min_words < 2:
        print("Minimum words shall be greater or equals to 2.")
        quit()
    if args.min_words > args.max_words:
        print("Maximum words shall be greater or equal to minimum words.")
        quit()

# Open dictionary files
dicts = []
for f in args.files:
    words = []
    try:
        with open(f) as fp:
            for line in fp:
                words.append(line.rstrip())
        dicts.append(words)
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
    if len(args.files) == 1 :
        # We combine within the lines of a single file
        for words_count in range(args.min_words, args.max_words + 1):
            for element in itertools.permutations(words, words_count):
                candidate = separator.join(element)
                print(candidate)
                # Print to output file if required
                if args.output_file is not None:
                    f.write(candidate + "\n")
    else:
        # We combine words from different files
        for words in list(itertools.product(*dicts)):
            for element in itertools.permutations(words):
                candidate = separator.join(element)
                print(candidate)
                # Print to output file if required
                if args.output_file is not None:
                    f.write(candidate + "\n")

if args.output_file is not None:
    f.close()
