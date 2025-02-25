#! /usr/bin/env python3

def kattis():
    stones = input()
    if (int(stones) % 2 == 0):
        print("Bob")
    else:
        print("Alice")

if __name__ == "__main__":
    kattis()