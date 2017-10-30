#!/usr/bin/python3
print("This line will be printed.")
x = 10
if(10 == x):
	print("x: ", x)
rawStr = r"\this is a \raw str"
print(rawStr)
print("0"+ 3*"1"+ "240"+ 2*"7"+ "50")

myID = int(7.5)
mySalary = float(20)
myComplex, myName = complex(5, 10), "Ahmed" 
print("My name is", myName, "My ID is" , myID, "My salary is", mySalary, "my complex is", myComplex)
print("My name is {} My ID is {} My salary is {} my complex is {}".format(myName, myID, mySalary, myComplex))
print("My name is {nm} My ID is {id} My salary is {slr} my complex is {cm}".\
format(slr=mySalary, id=myID, nm=myName, cm=myComplex))
print("My name is "+ str(myName) + " My ID is " + str(myID) + " My salary is " + str(mySalary) + " my complex is " + str(myComplex))
print("My name is %s My ID is %d My salary is %f my complex is "%(myName, myID, mySalary))