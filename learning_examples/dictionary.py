#!/usr/bin/python3
regionCode_D={}
regionCode_D["Cairo"] = "02"
regionCode_D["Alex"] = "03"
print(regionCode_D)	#{'Alex': '03', 'Cairo': '02'}

#Mapping: You can use dictionaries to map one set of values to another:
phonebook_D= {
	"Cairo office":"2468",
	"Alex office":"1357",
	"Zag office": "123456789"
}
print(phonebook_D)

#Dictionaries and Loops
for name, number in phonebook_D.items():	#for name, number in sorted(phonebook_D.items()): for sorted dictionary
	#print("Phone number of %s is %s ", name, number)	#Phone number of %s is %s  Zag office 123456789
	print("Phone number of %s is %s " %(name, number))	#Phone number of Cairo office is 2468

for name in phonebook_D.keys():		#for name in sorted(phonebook_D.keys()): for sorted dictionary key
	number = phonebook_D[name]
	print("Phone number of %s is %s " %(name, number))

#Note that keys does not process elements in any particular order. To process keys in alphabetical order, use sorted:
#sortedKeys = phonebook_D.keys().sort()	#'dict_keys' object has no attribute 'sort'
sortedKeys = sorted(phonebook_D.keys())
print(type(sortedKeys))
#sortedKeys.sort()

for name in sortedKeys:
	number = phonebook_D[name]
	print("Phone number of %s is %s " %(name, number))