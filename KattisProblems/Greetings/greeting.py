#! /usr/bin/env python3

def solution(inptHey):
    newHey = ""
    newHey = newHey + "h"
    for e in range((len(inptHey) - 2) * 2):
        newHey = newHey + "e"
    newHey = newHey + "y"

    return newHey

def kattis():
    inpt = input()
    print(solution(inpt))

if __name__ == "__main__":
    kattis()