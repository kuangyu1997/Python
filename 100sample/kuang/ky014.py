#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdout 
n = raw_input('Please enter a number:\n')
print 'n = %d' % n

for i in range(2,n + 1):
    if n % i == 0:
        n = n / i
        
