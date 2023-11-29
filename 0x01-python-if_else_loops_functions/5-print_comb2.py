#!/usr/bin/python3
for x in range(100):
    if x == 99:
        print('99')
        break
    print("{:02d},".format(x), end=' ')
