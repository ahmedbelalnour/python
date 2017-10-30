#!/usr/bin/python3
g_var=5

def try_to_set_global_var(value):
	g_var = value
	#print("local g_var = ", str(g_var))

def set_g_var(value):
	#global g_var = value 	#Error: invalid syntax
	global g_var
	g_var = value

def print_g_var():
	print(g_var)

print_g_var()				#g_val = 5, print 5 
try_to_set_global_var(20)	#g_val = 5, and local variable created inside the function called g_var = 20
print_g_var()				#g_val = 5, print 5 
set_g_var(40)				#g_val = 40
print_g_var()				#g_val = 40, print 40