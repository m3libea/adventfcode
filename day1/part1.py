#!/usr/bin/python
import re
file = open("input.txt").read()

o_par = len(re.findall("\(",file))
c_par = len(re.findall("\)",file))

print o_par - c_par