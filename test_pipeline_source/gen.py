#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
filename = 'message_and_key.txt' if len(sys.argv) <= 1 else sys.argv[1]

f = [[], []]
for i in range(4):
    f[0].append(open('m%s' % i, 'w'))
for i in range(4):
    f[1].append(open('k%s' % i, 'w'))
for i in range(2):
    for j in range(4):
        f[i][j].write('v2.0 raw\n')

with open(filename, 'r') as fr:
    for line in fr:
        nowline = line.strip().split(' ')
        for i in range(2):
            for j in range(4):
                f[i][j].write(nowline[i][8 * j: 8 * (j + 1)] + '\n')
