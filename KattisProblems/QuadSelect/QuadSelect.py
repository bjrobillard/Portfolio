#! /usr/bin/env python3

def solution(x,y):
    quadrant = 0
    if (int(x) > 0):
        if (int(y) > 0):
            quadrant = 1
        else:
            quadrant = 4
    else: 
        if (int(y) > 0):
            quadrant = 2
        else:
            quadrant = 3
    return quadrant

def kattis():
    x = input()
    y = input()
    print(solution(x,y))

if __name__ == "__main__":
    kattis()
