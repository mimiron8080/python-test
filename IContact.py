#!/usr/bin/python
# Filename: IContact.py

import cPickle as p
import os

_contactListFile = 'IContact.data'

class Contact:
      '''Represent the contact information!'''
      def __init__(self, name, phone_number, e_mail):
	  self.name = name
	  self.phone_number = phone_number
	  self.e_mail = e_mail

      def GetInfo(self, option):
	  if option == 'a':
	     print '''Name: %s \nPhone: %s \nE-mail: %s''' % (self.name, self.phone_number, self.e_mail)
	  if option == 'p':
	     print '''Name: %s 
Phone: %s''' % (self.name, self.phone_number)
	  if option == 'e':
	     print '''Name: %s
E-mail: %s''' % (self.name, self.e_mail)

def OpenFile():
    if os.path.exists('/Users/air/Desktop/python test/'+ _contactListFile):
       f = file(_contactListFile)
       print 'suc'
    else:
       f = file(_contactListFile, 'w')
       print 'failed'
    contactlist = p.load(f)
    f.close()
    return contactlist

def SaveFile(contactlist):
    f = file(_contactListFile)
    p.dump(contactlist, f)
    f.close()

def Insert():
    name = raw_input('Input name:')
    phone = raw_input('Input phonen umber:')
    e_mail = raw_input('Input e-mail:')
    c = Contact(name, phone, e_mail)
    contactlist = OpenFile() 
    contactlist[name] = c
    SaveFile(contactlist)
    print 'Insert new contact successfully!'

def Search():
    print 'Search is yet completed!'

def Delete():
    n = raw_input('Input your name of the contact what you want to delete')
    contactlist = OpenFile()
    for name, phone, email in contactlist:
 	if name == n:
	   del contactlist[name]
    SaveFile(contactlist)
    print 'Delete is yet completed!'

def main():
    option = raw_input('''Please input following option to chose what you want to do:
n- insert new contact
s- search contact
d- delete contact
q- quit\n''')
    
    if option == 'n':
 	Insert()
    elif option == 's':
	Search()
    elif option == 'd':
	Delete()
    elif option == 'q':
	return

while True:
	option = raw_input('''Please chose what to do:
w- Use this system
i- Get Info about this 
q- Quit\n''')
	if option == 'w':
	   main()
	elif option == 'i':
	   print '''Bexion co. Ltd 2014.07.15 Version 1.0.0'''
	elif option == 'q':
	   break
