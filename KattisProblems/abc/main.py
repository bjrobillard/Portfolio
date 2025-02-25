#! /usr/bin/env python3

def main():
    num = [int(x) for x in input().split()]
    num.sort()
    c = input()
    for i in range(3):
        print(num[ord(c[i]) - ord('A')], end=" ")
        
    print()


if __name__ == "__main__":
    main()