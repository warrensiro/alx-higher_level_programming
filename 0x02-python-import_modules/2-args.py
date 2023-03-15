#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print((len(argv) - 1), "arguments.")
    elif len(argv) == 2:
        print((len(argv) - 1), "argument:")
        for i  in argv:
            print("{} : {}".format(argv.index(i) + 1, str(i + 1)))
    elif len(argv) > 2:
        print((len(argv) - 1), "arguments:")
        for i in argv:
            print("{} : {}".format(argv.index(i) + 1, str(i + 1)))
