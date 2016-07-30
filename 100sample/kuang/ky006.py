#!/usr/bin/python
# -*- coding: UTF-8 -*-

#方法一
def fib(n):
	a,b = 0,1
	for i in range(n):
		a,b = b,a+b
	return a

print fib(10)

#方法二,使用递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print fib(10)

#方法三(如果你需要输出指定个数的斐波那契数列，可以使用以下代码)
def fib(n):
    if n == 1:
        return [1]        
    if n == 2:
        return [1,1]
    l = [1,1]
    for i in range(2,n):
        l.append(l[-2] + l[-1])
    return l

print fib(10)
