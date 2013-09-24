"""Solution to an exercise in Think Python.

Author:Emily Guthrie
"""


def print_Grid(row,col):
    top='+ - - - - '
    mid='|         '
    for x in range (0,row):
        print top*col,'+'
        print mid*col,'|'
        print mid*col,'|'
        print mid*col,'|'
        print mid*col,'|'
    print top*col,'+'
print_Grid(2,2)
print_Grid(4,4)
