#!/usr/bin/python
file = open("input.txt").read().split("\n")

total = 0

for line in file:
	values = line.split("x")
	l = int(values[0])
	w = int(values[1])
	h = int(values[2])
	smallest_side = sorted([l,w,h])[:2]
	parcial = l*w*h + 2*smallest_side[0] + 2*smallest_side[1]
	total+=parcial

print total


