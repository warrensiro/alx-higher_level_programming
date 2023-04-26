#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as ex:
        sys.stderr.write(f"Exception: {ex}\n")
        result = None
    else:
        return result
