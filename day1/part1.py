#!/usr/bin/python
import re

file = open("input.txt").read()

o_param = len(re.findall("\(",file))
c_param = len(re.findall("\)",file))

print o_param - c_param