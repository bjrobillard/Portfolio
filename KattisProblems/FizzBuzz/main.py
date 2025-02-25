#! /usr/bin/env python3

def solution(x, y, numb):
    if numb == 0:
        return
    if numb % x == 0 and numb % y == 0:
        print("FizzBuzz")
    elif numb % x == 0:
        print("Fizz")
    elif numb % y == 0:
        print("Buzz")
    else:
        print(numb)

def kattis():
    inpt = []
    inpt = input().split()
    numInpt = [eval(i) for i in inpt] # changing all string elems in list to int
    for i in range(numInpt[2] + 1):
        # print(i)
        solution(numInpt[0], numInpt[1], i)

if __name__ == "__main__":
    kattis()