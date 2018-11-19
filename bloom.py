"""

This is the implementation of a Bloom Filter (https://en.wikipedia.org/wiki/Bloom_filter)
It is a lightweight and memory-efficient way of storing data - in this case which memes
have already been posted to the group.

There is a high probability you don't need to change anything in this file.

Method checkfull() checks the amount of ones in the filter (8192 is the default array size, initialized with zeros)
Method checkp() checks the probability of returning a false positive.

If the filter is filled in over 75% or the probability is unsatisfactory, flush() its memory.

insert() and find() do not require an explanation - any valid string can be inserted and queried.

getIndex() helps with the aforementioned functions do their work

getTable() and writeTable() are employed so that the Filter can be stored in a file

setTable() is for debugging only

DISCLAIMER: The filter is slightly biased towards field table[size-1] due to the workaround in line 76, but in this
scope it hardly makes any difference

"""
import hashlib
import math
import sys

size = 8192
exponent = 13
amount = 20
class Bloom:
    def __init__(self):
        self.table = [0 for i in range(size)] #2E13

    def checkfull(self):
        count = 0
        for i in self.table:
            if i == 1:
                count += 1
        return count

    def checkp(self):
        count = 0
        x = 100000
        for i in range(x):
            if self.find(str(i)) == 1:
                count += 1
        n = count*100/x
        print("Probability of false positive is:", n,"%", file=sys.stderr)

    def insert(self, value):
        for i in range(amount):
            index = self.get_index(value)
            self.table[index] = 1
            value += "a"
            
    def flush(self):
        for i in range(len(self.table)):
            self.table[i] = 0

    def find(self, value):
        for i in range(amount):
            index = self.get_index(value)
            if self.table[index] == 0:
                return 0
            value += "a"
        return 1

    def get_index(self, value):
        m = hashlib.md5()
        m.update(value.encode('utf-8'))
        index = round(int(m.hexdigest(), 16) / math.pow(2, 128-exponent))
        if index == size:
            index = size-1
        return index

    def getTable(self, file):
        n = file.readline()
        for i in range(min(len(self.table), len(n))):
            self.table[i] = int((n[i]))

    def setTable(self, file, n=size): #for manual use only
        s = ''
        for i in range(n):
            s += '0'
        file.write(s)

    def writeTable(self, file):
        s = ''
        for c in self.table:
            s += str(c)
        file.write(s)