#!/usr/bin/python
# Filename: while.py

number = 23
running = True
while running:
  guess = int(raw_input('Enter an integer : '))
  if guess == number:
    print 'You got it, buddy'
    running = False #this cause the while loop to stop
  elif guess < number:
    print 'No, it is a little higher than that'
  else:
    print 'No, it is a little lower than that'
else:
  print 'The while loop is over'

print 'Done!'
