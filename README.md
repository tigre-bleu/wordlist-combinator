# Description

Simple tool to merge different words into a single one with customized separators. This tool was designed to build password candidates from a dictionnary of words that could be part of the password.

The tool will create all possible permutations of N words (N varying between a customized minimum and maximum. Default is 3) with all defined separators character (Default is no character, `-` and `_`).

# Usage

```
usage: wordlist-combinator.py [-h] [-min [MIN_WORDS]] [-max [MAX_WORDS]] [-s [N]] file

Combine a list of words in a list of combined words with separators

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -min [MIN_WORDS], --min-words [MIN_WORDS]
                        Minimum words to combine together. Default is 3
  -max [MAX_WORDS], --max-words [MAX_WORDS]
                        Maximum words to combine together. Default is 3
  -s [N], --separators [N]
                        Separators between combined words. Default is "-_". Empty separator is always included.

```
