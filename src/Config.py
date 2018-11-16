import glob
import sys
#    files = glob.glob('../data/*.frac')

def getConfigDict():
    config_dict = {}
    file = open(sys.argv[2])
    for line in file:
        parts = line.lower().split(' ')
        config_dict[parts[0]] = parts[len(parts) - 1].replace("\n", "")
    return config_dict

