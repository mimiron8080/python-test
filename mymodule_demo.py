#!/usr/bin/python
# Filename: mymodule_demo.py

import mymodule

print 'This is dir() of itself\n',dir(),'\n'
mymodule.sayhi()
print 'Version',mymodule.version
print 'This is dir() of mymodule\n',dir(mymodule)
