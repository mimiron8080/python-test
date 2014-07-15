#!/usr/bin/python
# Filename: assert.py

mylist = ['item1','item2','item3']

for item in mylist:
	print item
i = len(mylist)
while i > 0:
	print 'Item is %s' % mylist[i-1]
	assert len(mylist) >= 1
	print 'POP item is %s' % mylist.pop()
	i -= 1
assert len(mylist) >= 1
