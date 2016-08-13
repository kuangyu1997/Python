#!/usr/bin/python
# -*- coding: UTF-8 -*-

for n in range(101,1000):
    i = i / 100
    j = i / 10 % 10
    k = i % 10
    if n == i** 3 + j ** 3 + k ** 3:
        print n



