#!/usr/bin/python3
def islower(c):
    ch = ord(c)
    if ch in range(97, 123):
        return True
        print("{:c} is lower".format(ch))
    else:
        return False
        print("{:c} is upper".format(ch))
