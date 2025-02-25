#! /usr/bin/env python3

def solution(eyes, nose, mouth):
    return int(eyes) * int(nose) * int(mouth)


def kattis():
    inpt = []
    # for num in input():
    #     inpt.append(num)
    inpt = input().split(" ")
    # print(inpt)
    print(solution(inpt[0], inpt[1], inpt[2]))
        
if __name__ == "__main__":
    kattis()