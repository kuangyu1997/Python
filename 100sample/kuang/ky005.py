#!/usr/bin/python
# -*- coding: UTF-8 -*-

#参考代码：
l = []
for i in range(3):
    x = int(raw_input('integer: '))
    l.append(x)

l.sort()
print l

#自己编的代码：
x = int(raw_input('x: '))
y = int(raw_input('y: '))
z = int(raw_input('z: '))
if x > y:
    a = x
    x = y
    y = a

if x > z:
    b = x
    x = z
    z = b

if y > z:
    c = y
    y = z
    z = c

print x,y,z



