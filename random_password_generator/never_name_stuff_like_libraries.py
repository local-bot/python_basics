#! /usr/share/env python3

import random
import string

passwd = ''

for i in range(35):
    passwd += passwd.join(string.printable[random.randint(1,70)])


print(passwd)
