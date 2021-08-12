#!/usr/bin/env python

def loding():
    import sys
    import time

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor


    spinner = spinning_cursor()
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
