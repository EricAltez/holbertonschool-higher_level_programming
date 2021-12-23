#!/usr/bin/python3
import calculator_1 as ca
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, ca.add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, ca.sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, ca.mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, ca.div(a, b)))
