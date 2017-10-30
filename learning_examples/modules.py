#!/usr/bin/python3
import MyArithmatic
#print(addTwoNumbers(5,6))				#Error: name 'MyArithmatic' is not defined
print(MyArithmatic.addTwoNumbers(5,6))	#print: 11

from MyArithmatic import *
#print(MyArithmatic.addTwoNumbers(5,6))	#Error: name 'MyArithmatic' is not defined
print(addTwoNumbers(5,6))				#print: 11

from MyArithmatic import addTwoNumbers
#print(MyArithmatic.addTwoNumbers(5,6))	#Error: name 'MyArithmatic' is not defined
print(addTwoNumbers(5,6))				#print: 11
import urllib	#you can write import in any part of the code