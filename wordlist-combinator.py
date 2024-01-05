#!/usr/bin/env python3
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='Combines a list of words in a list of combined words with separators. \
        Example: wordlist-combinator.py -min 2 -max 4 -s \"_-.\" -o merged.lst names.lst cities.lst')
parser.add_argument('-min', '--min-words', type=int, help='Minimum words to combine together. Default is 2', nargs='?', default=2)
parser.add_argument('-max', '--max-words', type=int, help='Maximum words to combine together. Default is 3', nargs='?', default=3)
parser.add_argument('-c', '--capitalize', action='store_true', help="Add candidates with both normal words and capitalized words")
parser.add_argument('-s', '--separators', metavar='N', type=str, nargs='?', help='Separators between combined words. Default is \"-_\". Empty separator is always included. Example: \"_-.,\"', default=["-","_"])
parser.add_argument('-pre', '--prepend', action='store_true', help='Add candidates with separators as first character')
parser.add_argument('-post', '--postpend', action='store_true', help='Add candidates with separators as last character')
parser.add_argument('-o', '--output-file', type=str, help='Outputs to a file instead of stdout', nargs='?')
parser.add_argument('files', help='Combine all lines of all files', nargs='+')
args = parser.parse_args()

if args.min_words < 2:
    print("Minimum words shall be greater or equals to 2.")
    quit()
if args.min_words > args.max_words:
    print("Maximum words shall be greater or equal to minimum words.")
    quit()

def output_candidate(candidate):
    # Print to output file if required, otherwise to stdout
    if args.output_file is not None:
        f.write(candidate + "\n")
    else:
        print(candidate)

# Open dictionary files
words = []
for f in args.files:
    try:
        with open(f) as fp:
            for line in fp:
                words.append(line.rstrip())
                # If capitalize flag then add also the capitalized word
                if (args.capitalize):
                    words.append(line.rstrip().capitalize())
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

generated_count = 0

for words_count in range(args.min_words, args.max_words + 1):
    for words_pattern in itertools.permutations(words, words_count):
        for separators_pattern in itertools.combinations_with_replacement(separators, words_count -1):
            candidate = ""
            i = 0
            # Build candidate
            while i < len(words_pattern):
                candidate = candidate + words_pattern[i]
                if i < len(separators_pattern):
                    candidate = candidate + separators_pattern[i]
                i = i+1
            generated_count = generated_count + 1
            
            output_candidate(candidate)

            # Add pre and/or post separators if required
            if args.prepend and args.postpend :
                for pre in separators:
                    if pre != "":
                        for post in separators:
                            if post != "":
                                output_candidate(pre + candidate + post)
            elif args.prepend :
                for separator in separators:
                    if separator != "":
                        output_candidate(separator + candidate)
            elif args.postpend :
                for separator in separators:
                    if separator != "":
                        output_candidate(candidate + separator)

if args.output_file is not None:
    print(f'%s candidates generated' % generated_count)
    f.close()
