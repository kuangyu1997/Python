#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(raw_input('year:'))
mouth = int(raw_input('mouth:'))
day = int(raw_input('day:'))
mouths = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < mouth < 13:
    sum = mouths[mouth-1]
else:
    print 'mouth error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (mouth >= 2):
    sum += 1
print 'It is the %dth day.' % sum
    


