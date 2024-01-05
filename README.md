# Description

Simple tool to merge different words into a single one with customized separators. This tool was designed to build password candidates from a dictionnary of words that could be part of the password.

The tool will create all possible permutations of N words (N varying between a customized minimum and maximum. Default is 2 and 3) with all defined separators character (Default is no character, `-` and `_`).

Some modifiers can be added to capitalize words, and add separators as prefix and/or suffix.

# Usage

```
usage: wordlist-combinator.py [-h] [-min [MIN_WORDS]] [-max [MAX_WORDS]] [-c] [-s [N]] [-pre] [-post] [-o [OUTPUT_FILE]] files [files ...]

Combines a list of words in a list of combined words with separators. Example: wordlist-combinator.py -min 2 -max 4 -s "_-." -o merged.lst names.lst cities.lst

positional arguments:
  files                 Combine all lines of all files

options:
  -h, --help            show this help message and exit
  -min [MIN_WORDS], --min-words [MIN_WORDS]
                        Minimum words to combine together. Default is 2
  -max [MAX_WORDS], --max-words [MAX_WORDS]
                        Maximum words to combine together. Default is 3
  -c, --capitalize      Add candidates with both normal words and capitalized words
  -s [N], --separators [N]
                        Separators between combined words. Default is "-_". Empty separator is always included. Example: "_-.,"
  -pre, --prepend       Add candidates with separators as first character
  -post, --postpend     Add candidates with separators as last character
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        Outputs to a file instead of stdout
```
