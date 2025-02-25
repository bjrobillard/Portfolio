#! /usr/bin/env python3

def kattis():
    word = input()
    newW = ""
    for i in range(3):
        newW = newW + word + " "

    print(newW)

if __name__ == "__main__":
    kattis()