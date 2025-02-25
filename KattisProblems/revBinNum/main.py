#! /usr/bin/env python3

def main():
    startNum = input()
    binNum = bin(int(startNum))
    listnum = binNum.strip("0b")
    rev = [x for x in listnum]
    rev.reverse()
    newBin = "".join(rev)
    value = int(newBin,2)
    print(value)
    


if __name__ == "__main__":
    main()