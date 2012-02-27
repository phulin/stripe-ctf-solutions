import sys
import string
import json
import os

def getline():
    return sys.stdin.readline()[:-1]

def firststr(s):
    return string.split(s, "\t")[0]

if os.path.exists("dict"):
    f = open("dict", "r")
    times = json.loads(f.read())
    f.close()
    f = open("dict", "w")
else:
    times = dict()
    f = open("dict", "w")

nextln = getline()
while True:
    letters = nextln
    if letters == "":
        break
    nextln = getline()
    stack = list()
    while firststr(nextln).isdigit() and not nextln.isdigit():
        stack.append(nextln)
        nextln = getline()
    t2 = int(firststr(stack.pop()))
    t1 = int(firststr(stack.pop()))
    diff = t2 - t1
    if diff > 15:
        value = 1
    else:
        value = 0

    if letters in times:
        times[letters] += value
    else:
        times[letters] = value

f.write(json.dumps(times))
f.close()
