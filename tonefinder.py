#!/usr/bin/python3
from __future__ import print_function

import sys
import warnings

import madmom
import numpy as np
from scipy.linalg import circulant

NOTENAME = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
DIATONIC_SYSTEM = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]

# The main function.
def main(args):
    if len(sys.argv) < 2:
        print("Detects the key signature of a song.\n\nUsage: %s filename.mid" % sys.argv[0])
        sys.exit(-1)

    # parse the midi information into a numpy array
    parsed_midi = madmom.utils.midi.process_notes(args[0])

    # get a numpy array of notes
    notes = parsed_midi[:,1]

    # f is a lambda function that maps each notes to it's key
    keymapper = np.vectorize(lambda x : (int) (x % 12))
    basenotes = keymapper(notes)

    # get the counts of all unique notes
    unique, counts = np.unique(basenotes, return_counts=True)

    # create a row matrix of all the counts of the notes 
    note_counts = np.zeros(12)
    for key, val in list(zip(unique, counts)):
        note_counts[key] = val
    note_counts = np.matrix(note_counts).T

    # create a circular square matrix based on a diatonic scale
    multiplier = np.matrix(circulant(DIATONIC_SYSTEM)).T

    # perform a matrix multiplication to get the relative key usage
    result = np.matmul(multiplier, note_counts)

    # find the highest index
    index = np.argmax(result)

    # print out the proposed key signature 
    print("The key signature of the song is", NOTENAME[index])

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main(sys.argv[1:])