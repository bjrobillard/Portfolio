#! /usr/bin/env python3
from sys import stdin

def main():
    inpt = stdin.readlines()
    # print(inpt)
    for i in range(4):
        inpt[i] = inpt[i].strip()
        # print(inpt[i])

    name = inpt[0]
    a = int(inpt[1])
    b = int(inpt[2])
    sORj = int(inpt[3])

    if a > b:
        print("VEIT EKKI")
    elif a - b == sORj:
        print("JEDI")
    elif a - b != sORj:
        print("SITH")
    
if __name__ == "__main__":
    main()