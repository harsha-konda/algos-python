# implement a data structures

# insert(A,3000)
# insert(B,2000)

# get() A with 3/5
# get() B with 2/5

from random import random

class GetRandom:
    def __init__(self):
        self.r = [0]
        self.keys = []

    def insert(self,key,value):
        end = self.r[-1]+value
        self.r.append(end)
        self.keys.append(key)

    def search(self,num):
        i,j = 0,len(self.r)-1
        while(i<=j):
            mid = (i+j)//2
            if num >= self.r[mid] and num<=self.r[mid+1]:
                return mid

            if num < self.r[mid]:
                j = mid
            else:
                i = mid+1


    def get(self):
        num = int(random()*len(self.r[-1]))
        index = self.search(num)
        return self.keys[index]

c = GetRandom()
c.insert("A" , 2000)
c.insert("B",3000)

