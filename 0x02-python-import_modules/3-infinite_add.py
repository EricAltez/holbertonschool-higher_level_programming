#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv)
    res = 0
    for i in range(1, leng):
        res = res + (int(argv[i]))
    print("{:d}".format(res))
