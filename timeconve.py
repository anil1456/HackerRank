#!/bin/python3
import sys
s = raw_input()
a=int(s[:2])
b=s[-2:]
if b == "AM":
    if a==12:
      print("{}{}".format(a-12,s[2:-2]))
    else:
      print(s[:-2])
elif b == "PM":
    if a==12:
        print("{}{}".format(a,s[2:-2]))
    else:
        print("{}{}".format(a+12,s[2:-2]))
