# Description

Simple tool to merge different words into a single one with customized separators. This tool was designed to build password candidates from a dictionnary of words that could be part of the password.

The tool can work in two ways:

**A single file is provided as parameter:**

In that cas, the tool will create all possible permutations of N words (N varying between a customized minimum and maximum. Default is 3) with all defined separators character (Default is no character, `-` and `_`).

**Multiple files are provided as parameter:**

In that case the tool will create all the possible permutations with one word (and only one) from each file with all defined separators character (Default is no character, `-` and `_`). `-min` and `-max` parameters are not used in that case as the number of combined words is always equal to the number of files provided.

# Usage

```
usage: wordlist-combinator.py [-h] [-min [MIN_WORDS]] [-max [MAX_WORDS]] [-s [N]] [-o [OUTPUT_FILE]]
                              files [files ...]

Combines a list of words in a list of combined words with separators. Example: wordlist-combinator.py -min 2 -max 4
-s "_-." -o merged.lst example.lst

positional arguments:
  files                 if single argument: combine all lines, if multiple arguments: combine lines from all files

optional arguments:
  -h, --help            show this help message and exit
  -min [MIN_WORDS], --min-words [MIN_WORDS]
                        Minimum words to combine together (if single file is provided). Default is 3
  -max [MAX_WORDS], --max-words [MAX_WORDS]
                        Maximum words to combine together (if single file is provided). Default is 3
  -s [N], --separators [N]
                        Separators between combined words. Default is "-_". Empty separator is always included.
                        Example: "_-.,"
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        Outputs to a file in addition to stdout
```
