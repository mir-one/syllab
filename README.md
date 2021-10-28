# Syllab

Simple Python 2/3 package for breaking Russian words into syllables.

## Installation

Type in console:

```
pip install git+https://github.com/mir-one/syllab
```

## API

Function *split_word* splits a word aand returns a list of syllables. 

Function *split_words* processes the list of words and return the list of syllables and spaces for word separation.

## Usage


Example:

```
import syllab

sx = syllab.split_words(u"Голодная кошка ловит мышку".split())
print('|'.join(sx))
```

Result:

```
Го|лод|на|я| |кош|ка| |ло|вит| |мыш|ку
```
