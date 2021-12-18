# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:06:34 2021

@author: lawre
"""
'hashmap of a hashmap'

from linkedlist import doublylinkedlist

class hashmap(object):
    def __init__(self, size=0, capacity=20):
        bucketlist = []
        for i in range(capacity): [bucketlist.append(doublylinkedlist())]
        self.buckets = bucketlist
        self.size = size
        self.capacity = capacity
    
    def hasher(self, key):
        return hash(key)*2 % self.capacity
    
    def insert(self, key, data):
        hashkey = self.hasher(key)
        self.buckets[hashkey].lappend(key,data)
        self.size+=1
    
    def remove(self, key):
        hashkey = hash(key) % self.capacity
        self.buckets[hashkey].deletekeys(key)
        self.size-=1
        
    def getdata(self, key):
        hashkey = self.hasher(key)
        bucket = self.buckets[hashkey]
        datanode = bucket.findval(key)
        return datanode.realdata
        
    
    def printmap(self):
        print("Selection of Map:")
        occupied = []
        for i in range(len(self.buckets)):
            node = self.buckets[i].head
            count = 0;
            while node:
                count+=1
                node = node.next
            if count == 1:
                occupied.append("%a"%i)
            elif count > 1:
                occupied.append("{}[{}]".format(i,count))
        print(occupied)
            