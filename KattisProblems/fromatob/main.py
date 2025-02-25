#! /usr/bin/env python3

def main():
    # inpt = input().split()
    a, b = map(int, input().split())
    # print("A:", a)
    # print("B:", b)
    opers = 0
    
    while a != b:
        if a > b and a % 2 == 0:
            a //= 2
            opers += 1
            
        else: 
            a += 1
            opers += 1
    # while a != b:
    #     if a > b and not a & 1:  # Using bitwise AND to check if a is even
    #         a >>= 1  # Using bitwise right shift for division by 2
    #     else:
    #         a += 1

    # while a != b:
    #     if a > b and a % 2 == 0:
    #         a //= 2
        
    #     else:
    #         a += 1
        

    print(opers)
    # Not fast enough for last two cases of kattis tests


if __name__ == "__main__":
    main()