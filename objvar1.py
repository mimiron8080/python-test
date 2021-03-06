#!/usr/bin/python
# Filename: objvar.py

class Person:
    '''Represent a person'''
    population = 0
    
    def __init__(self, name):
        self.name = name
        print '(Initializing %s)' % self.name
        
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
   
    def __del__(self):
	'''I am dying.'''
	print '%s says bye.' % self.name

	Person.population -= 1

	if Person.population == 0:
	    print 'I am the last one.'
	else:
	    print 'There are still %d people left.' % Person.population

    def sayHi(self):
	'''Greeting by the person.
	
	Really, that's all it does.'''
	print 'Hi, my name is %s.' % self.name

    def howMany(self):
 	'''Prints the current population.'''
	if Person.population == 1:
	   print 'I am the only person here.'
	else:
	   print 'We have %d persons here.' % Person.population

swaroop = Person('swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

kaka = Person('kaka')
kaka.sayHi()
kaka.howMany()

# swaroop.sayHi()
# swaroop.howMany()
kalam.sayHi()
kalam.howMany()

