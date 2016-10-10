# -*- coding:utf-8 -*-

import random

code = []

for i in range(1, 6):
    if i == random.randint(1, 5):
        code.append(str(random.randint(0, 9)))
    else:
        code.append(chr(random.randint(65, 90)))

print ''.join(code)
