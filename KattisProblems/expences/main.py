#! /usr/bin/env python3

def main():
    total = 0
    inpt = int(input()) # pointless input
    expenses = [int(x) for x in input().split()]
    for i in range(inpt):
        if "-" in str(expenses[i]):
            total = total + expenses[i]
    print(total * -1)

if __name__ == "__main__":
    main()