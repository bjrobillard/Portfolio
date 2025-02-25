#! /usr/bin/env python3
from collections import Counter

def main():
    letters = input()
    # print(letters)
    counter = Counter(letters)
    duplicates = [letter for letter in counter if counter[letter] > 1]
    # print(duplicates)
    if len(duplicates) == 0:
        print("1")
    else:
        print("0")
    

if __name__ == "__main__":
    main()