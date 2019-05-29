#!/usr/bin/python

import os

f = open('readmyself.py', 'r')
for line in f:
    print(line.rstrip('\n'))

f.close() # ALWAYS close a file that you open