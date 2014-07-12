#!/usr/bin/python
# Filename: func_key.py

def func(a,b=5,c=10):
    print 'a is',a, 'b is',b, 'c is',c


func(1)
func(3,7)
func(1,c=3)
func(c=3,a=2)
