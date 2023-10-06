#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("{} : {}".format(n, sys.argv[n]))
    else:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{} : {}".format(i, sys.argv[i]))

