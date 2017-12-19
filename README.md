# pySynsets
A python command line tool to inspect "Synsets" of ILSVRC2012

## Usage
Download **ILSVRC2012_devkit_t12.tar.gz** from http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads.
Extract **meta.mat** and put it in the same folder as **pySynsets.py**

**pySynsets.py -h**
```
usage: pySynsets.py [-h]
                    (-verbose | -table | -showField SHOWFIELD | -expand EXPAND)
                    [-ILSVRC2012_ID ILSVRC2012_ID] [-WNID WNID] [-words WORDS]
                    [-gloss GLOSS] [-listChildren]

A tool to inspect Synsets of ILSVRC2012

optional arguments:
  -h, --help            show this help message and exit
  -verbose              display everything
  -table                display in a table
  -showField SHOWFIELD  display selected field only
  -expand EXPAND        expand children (display selected field only)
  -ILSVRC2012_ID ILSVRC2012_ID
                        'ILSVRC2012_ID' is an integer ID assigned to each
                        synset. All the low level synsets are assigned to an
                        ID between 1 and 1000. All the high level synsets have
                        ID higher than 1000.
  -WNID WNID            WNID' is the WordNet ID of a synset. It is used to
                        uniquely identify a synset in ImageNet or WordNet. The
                        tar files for training images are named using WNID.
                        Also it is used in naming individual training images.
  -words WORDS          Search given text in 'words'
  -gloss GLOSS          Search given text in 'gloss'
  -listChildren         list children instead the item
```
## Same examples
1. List all items that cantain string "cat" in field "words" in a table
```
pySynsets.py -words cat -table
```
2. Get verbose information about WNID "n02509815"
```
pySynsets.py -WNID n02509815 -verbose
```
3. Expand WNID 'n02121620' (cat) in to a hierarchy tree
```
pySynsets.py -WNID n02121620 -expand words
```
