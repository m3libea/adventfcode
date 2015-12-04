#!/usr/bin/python

file = open("input.txt").read()

o_par = 0
c_par = 0
i = 0;

while(o_par - c_par != -1):
	if(file[i] == "("):
		o_par += 1
	else:
		c_par += 1
	i+=1

print len(file[:i])