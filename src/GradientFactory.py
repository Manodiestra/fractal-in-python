from GreyScale import GreyScale
from RedBlue import RedBlue
import sys


def makeGradient():
    # Make and return a gradient object.
    if len(sys.argv) >= 3:
        if sys.argv[2] == "Greyscale":
            g = GreyScale()
            return g
        elif sys.argv[2] == "RedBlue":
            g: RedBlue = RedBlue()
            return g
        else:
            print("Default gradient selected.")
            g = RedBlue()
            return g
    else:
        print("Default gradient selected.")
        g = RedBlue()
        return g