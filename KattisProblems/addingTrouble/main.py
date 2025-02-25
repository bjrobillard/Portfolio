#! /usr/bin/env python3

def main():
    inpt = input().split()
    numbers = [int(x) for x in inpt]
    if (numbers[0] + numbers[1]) == numbers[2]:
        print("correct!")
    else:
        print("wrong!")

if __name__ == "__main__":
    main()