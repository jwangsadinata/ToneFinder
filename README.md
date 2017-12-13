# ToneFinder

Tonefinder is a simple implementation of a program detecting the key signature of a midi file. It is written using the `madmom` package for midi parsing, along with `numpy` and `scipy` for processing. The idea is based on a matrix multiplication, counting the most common occurrence of notes in a diatonic scale. The accuracy is pretty decent, and can be improved a little bit more.

## Usage:
Install `madmom`, `numpy` and `scipy`, then run:
```
python3 tonefinder.py filename.mid
``` 
