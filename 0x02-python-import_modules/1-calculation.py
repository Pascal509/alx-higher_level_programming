#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

add_values = add(a, b)
sub_values = sub(a, b)
mul_values = mul(a, b)
div_values = div(a, b)

print("{:d} +i {:d} = {:d}".format(a, b, add_values))
print("{:d} - {:d} = {:d}".format(a, b, sub_values))
print("{:d} * {:d} = {:d}".format(a, b, mul_values))
print("{:d} / {:d} = {:d}".format(a, b, div_values))
