#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = 1
    num = 0
    while len(argv) != n:
        a = argv[n]
        num += int(a)
        n += 1
    print("{}".format(num))
