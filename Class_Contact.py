#!/usr/bin/python
# Filename: Class_Contact.py

import cPickle as p

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


c = Contact('wanghao','1561896137','420276072@qq.com')
cdic = {'wanghao',c}
f = file('IContact.data', 'w')
p.dump(cdic, f)
f.close()

f = file('IContact.data')
cdic = p.load(f)
for key, value in cdic:
    print 'key:%s value:%s' % (key, value)
