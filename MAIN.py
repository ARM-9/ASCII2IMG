#IMG <-> ASCII
__author__ = 'ARM_9'

from IMGTOASCII import IMGToASCII
from ASCIITOIMG import ASCIIToIMG


if __name__ == "__main__":
    path = input("Enter the path file you want converted:   ")

    if (path[len(path) - 3:] == "txt"):
        ASCIIToIMG(path)
    else:
        IMGToASCII(path)
