# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:59:37 2021

@author: lawre
"""

import random
from hashmap import hashmap

hmap1 = hashmap(10)

names = ["Chatime", "Emily", "Carolyn", "Jeffery", "Larry", "Angel", "Kaitlyn", "Isabelle"]


def hasher( key):
    return hash(key)*2 % hmap1.capacity

theinfo = []
for i in range(len(names)):
    ran = random.randint(0,100)
    name = random.choice(names)
    theinfo.append([name, ran, hasher(name)])
    hmap1.insert(name,ran)
    names.remove(name)
    

for i in theinfo:
    print(i)
    
print()
hmap1.printmap()
hmap1.buckets[14].printlist()
print()

emilydata= hmap1.getdata("Emily")
carolyndata= hmap1.getdata("Carolyn")
print("Emily", emilydata)
print("Carolyn", carolyndata)


