#!/usr/bin/python3
import sys


class n_queens:
        pass

if __name__ == '__main__':

    if len(sys.argv) is not 2:
        print("Usage: nqueens N")
        exit(1)

    if sys.argv[1].isdigit():
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            exit(1)
    else:
        print("N must be a number")
        exit(1)

    call = n_queens()
    call.n_queens(1, sys.argv[1])
