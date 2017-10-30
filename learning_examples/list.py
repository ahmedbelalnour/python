#!/usr/bin/python3
def printSeq(seq):
	for sq in seq:
		if sq == seq[-1]:
			print(sq + ".")
		else:
			print(sq, end=", ")

def printSeq2(seq):
	for sq in seq:
		print(sq, "\b, ", end="")
	print("\b\b. ")

devices_L = ["Mobile phone", "Laptop"]
printSeq2(devices_L)
devices_L.append("Mouse")
printSeq(devices_L)
poppedDevice = devices_L.pop()
print("Popped device = " + poppedDevice)
printSeq(devices_L)
laptopIndex = devices_L.index("Laptop")
print("Laptop index = "+ str(laptopIndex))
#devices_L[2]="Router"	#Error: list assignment index out of range
#devices_L += "Router"	#Error: can only concatenate list (not "str") to list
devices_L += ["Router"]
printSeq(devices_L)
devices_L.remove("Mobile phone")
printSeq(devices_L)
#devices_L.append("Mouse", "Keyboard")	#Error: append() takes exactly one argument (2 given)
devices_L.append("Mouse")
devices_L.append("Keyboard")
printSeq(devices_L)
devices_L.sort()
printSeq(devices_L)
devices_L.reverse()
printSeq(devices_L)
print(len(devices_L))
del(devices_L)
#printSeq(devices_L)	#Error: name 'devices_L' is not defined

devices_L=[]
#devices_L[0]="Laptop"	#Error: list assignment index out of range
print(devices_L)	#[]