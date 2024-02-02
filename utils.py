import os
import pandas as pd

# Write from a dictionary to a file
def writeDictionary(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write('%s;%s\n' % (key, value))

# Read all from a file to a dictionary
def readDictonary(filename):
    dictionary = {}
    if not os.path.isfile(filename):
        return dictionary

    with open(filename, 'r') as file:
        for line in file:
            key, value = line.split(';')
            # Check if the value is a float
            dictionary[key] = float(value)

    return dictionary

def mifs_caching_init(path, df_filename, discreteDf_filename, entropyFilename, jointEntropyFilename):
    discreteDf_filename = df_filename[:-4] + '_' + discreteDf_filename
    entropyFilename = df_filename[:-4] + '_' + entropyFilename
    jointEntropyFilename = df_filename[:-4] + '_' + jointEntropyFilename

    discreteDf = None
    try:
        discreteDf = pd.read_csv(path + discreteDf_filename)
    except FileNotFoundError:
        pass

    if discreteDf is None:
        entropyCache = {}
        jointEntropyCache = {}
    else:
        entropyCache = readDictonary(path + entropyFilename)
        jointEntropyCache = readDictonary(path + jointEntropyFilename)

    return discreteDf, entropyCache, jointEntropyCache, discreteDf_filename, entropyFilename, jointEntropyFilename


def mifs_caching_flush(path, entropyCache, jointEntropyCache, entropyFilename, jointEntropyFilename):
    writeDictionary(entropyCache, path + entropyFilename)
    writeDictionary(jointEntropyCache, path + jointEntropyFilename)