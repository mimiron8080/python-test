#!/usr/bin/python
# Filename: args.py

def powersum(power, *args):
	'''Return the sum of each argument raised to specified power.'''
	total = 0
	for i in args:
		total += pow(i, power)
		print 'i is %s pow(i, power) = %s' % (i,pow(i, power))
	return total

def ff(**args):
	

print powersum(2, 3, 4)
print powersum(2, 10)
