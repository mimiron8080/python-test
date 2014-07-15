#!/usr/bin/python
# Filename: repr.py

i = []
i.append('item')
print `i`

print repr(i)

print eval(repr(i))[0]
