#! /usr/share/env python3

import random
import string

'''
for i in string.printable():
    print(i)
'''

for i in range(12):
    print(string.printable[random.randint(1,127)])
    #  complete later...