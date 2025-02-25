#! /usr/bin/env python3
from sys import stdin

def main():
    inpt = stdin.readlines()
    # print(inpt)
    fbiLoc = ""
    for i in range(len(inpt)):
        # print(inpt[i])
        if "FBI" in inpt[i]:
            fbiLoc += str(i+1) + " "

    if fbiLoc == "":
        fbiLoc = "HE GOT AWAY!"
    print(fbiLoc)

if __name__ == "__main__":
    main()