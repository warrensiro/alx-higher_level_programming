#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(len(argv), "argument:")
        for i in argv:
            print("{} : {}".format(argv.index(i) + 1, i))
    elif len(argv) == 0:
        print(len(argv), "arguments.")
    elif len(argv) > 1:
        print(len(argv), "arguments:")
        for i in argv:
            print("{} : {}".format(argv.index(i) + 1, i))
