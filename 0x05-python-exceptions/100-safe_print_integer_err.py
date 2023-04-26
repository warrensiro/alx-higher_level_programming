#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as ex:
        sys.stderr.write(f"Exception {ex}")
        return False
    else:
        return True
