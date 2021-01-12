#!/usr/bin/python3

import sys

class n_queens:

    class __init(self):
        

if __name__ == '__main__':

    if len(sys.argv) is not 2:
        print("Usage: nqueens N")
        exit(1)

    if type(sys.argv) is not int:
        print("N must be a number")
        exit(1)

    if sys.argv < 4:
        print("N must be a number")
        exit(1)

    call = n_queens()
    call.n_queens(1, sys.argv[1])
