#!/usr/bin/python
# -*- coding: UTF-8 -*-

score = int (raw_input('intput score:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print '%d belong to %s' % (score,grade)

