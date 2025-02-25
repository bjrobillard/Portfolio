#! /usr/bin/env python3

def solution(num1, num2):
    newSecNum = int(num2) * 2
    newR2 = int(newSecNum) - int(num1)
    return newR2

def kattis():
    inpt = []
    inpt = input().split(" ")
    print(solution(inpt[0],inpt[1]))

if __name__ == "__main__":
    kattis()