#!/usr/bin/python3
#working with strings
#1. String Indexing and Slices
helloSong = "hello from the other side"
#			0, 1, 2, ............., 24
#			-25, -25, ............, -1
#when we use from to, the first number is included, the last number is not included
print(len(helloSong))	#print: 25
print(helloSong[1])		#Strat from the beginning and print second letter: e
print(helloSong[-2])	#Strat from the end and print second letter: d
print(helloSong[1:3])	#print: el
print(helloSong[3:1])	#print: empty space
print(helloSong[:3])	#print: hel
print(helloSong[3:])	#print: lo from the other side
print(helloSong[:-3])	#print: hello from the other s
print(helloSong[-3:])	#print: ide
print(helloSong[-3:-1])	#print: id
print(helloSong[-1:-3])	#print: empty space
#You can also use slices with lists
devices_L = ["LAptop", "Mobile phone", "Tablet", "Screen"]
print(devices_L[1:3])	#print: [Mobile phone", "Tablet"]

#2. String Capitalization Functions, output did not saved in the original string
print(helloSong.capitalize())	#print: Hello from the other side
print(helloSong.lower())		#print: hello from the other side
print(helloSong.upper())		#print: HELLO FROM THE OTHER SIDE
print(helloSong.swapcase())		#print: hELLO FROM THE OTHER SIDE
print(helloSong.title())		#print: Hello From The Other Side