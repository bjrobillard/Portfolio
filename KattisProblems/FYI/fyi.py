#! /usr/bin/env python3

def solution(num):
    if num.startswith("555"):
        return 1
    else:
        return 0

def kattis():
    inpt = input()
    # print(type(inpt))
    # print(inpt.rstrip(inpt[-4:-1]))
    # if inpt== -1: 
    #     print("0")
    # else:
    #     print("1")
    print(solution(inpt))

if __name__ == "__main__":
    kattis()