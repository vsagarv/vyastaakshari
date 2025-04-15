#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import regex
import random

# ----
# https://stackoverflow.com/questions/33068727/how-to-split-unicode-strings-character-by-character-in-python
# for text in [u'தமிழ்', u'हिंदी']:
#     print("\n".join(regex.findall(r'\X', text, regex.U)))
# 
# for text in [u"కల్పవృక్షంబు"]:
#     print("\n".join(regex.findall(r'\X', text, regex.U)))
# 
# ----

if len(sys.argv) < 3:
    print("usage: ", sys.argv[0], " <input_filename> <max_aksharams>")
    exit(-1)

inp_f = sys.argv[1]
maxlen = sys.argv[2]

f = open(inp_f, "r", encoding="utf-8")
lines = f.readlines()
n_lines = len(lines)
r = random.randint(0, n_lines-1)

l = lines[r]
l = ''.join(l.split())

chars = regex.findall(r'\X', l)
n = len(chars)
print("len = ", n)

maxlen = min(n, maxlen)

random_order = random.sample(range(0, maxlen), maxlen)
print(random_order)

for i in random_order:
    print(i+1, chars[i])  # i+1: human readable positions as 1-based and not 0-based
    input("Next ?")

input("Press enter to start giving the correct order")

new_l = ""
for i in range(0, maxlen):
    new_l = new_l + input()

print("Your order: ", new_l)

print("Actual order: ", l)

if new_l == l[0:maxlen]:
    print("Excellent !!")
else:
    print("Oops !!")
