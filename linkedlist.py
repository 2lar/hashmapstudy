# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 00:08:49 2021

@author: lawre
"""

class Node:
    def __init__(self, data, realdata):
        self.data = data #same thing as key, I just got lazy editing it
        self.realdata = realdata
        self.next = None
        self.prev = None
    
    def nodedata(self):
        print(self.data)
    
    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.data)
        else:
            return "<Node key: %s data: %d>" % (self.key, self.data)

class doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    #iterator
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            
    #this is an iterator version taking it in reverse
    #this does not modify the list into a reverse order
    #there is a function call reverselist() to reverse the order
    def __reversed__(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev
    
    #copy and delete
    def deletelist(self):
        current = self.head
        while current:
            nxt = current.next
            del current.data
            current = nxt
        self.head = self.tail = None
        self.size = 0
            
    def copylist(self, other):
        if not self.empty():
            self.deletelist()
        if other.head is not None:
            current = other.head
            while current:
                self.lappend(current.data)
                current = current.next
            self.size = other.size
            
    #Functions that check within
    def empty(self):
        if self.head is None:
            return True
        return False
    
    def findval(self,val):
        current = self.head
        if current is None:
            print("No value because list is empty")
            return
        counter = 0
        while current:
            if current.data == val:
                print("This value is in position/index in bucket:",counter)
                return current
            counter+=1
            current = current.next
        print("No node contains this value")
        return
    
    def high(self):
        if self.empty(): return
        highval, current = self.head.data, self.head.next
        while current:
            if current.data > highval:
                highval = current.data
            current = current.next
        print("The high value is:",highval)
    
    def findhigh(self):
        if self.empty(): return
        highval, current = self.head.data, self.head.next
        while current:
            if current.data > highval:
                highval = current.data
            current = current.next
        return highval
        
    def low(self):
        if self.empty(): return
        lowval, current = self.head.data, self.head.next
        while current:
            if current.data < lowval:
                lowval = current.data
            current = current.next
        print("The low value is:",lowval)
    
    def findlow(self):
        if self.empty(): return
        lowval, current = self.head.data, self.head.next
        while current:
            if current.data < lowval:
                lowval = current.data
            current = current.next
        return lowval
    
    #Functions that modify the list
    def lappend(self,newkey, newdata):
        
        new_node = Node(newkey, newdata)
        
        if self.head is None:
            self.head = self.tail = new_node
            self.size+=1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size+=1
        return
    
    def pushfront(self, newkey, newdata):
        new_node = Node(newkey, newdata)
        
        if self.head is None and self.tail is None:
            self.head = self.tail = new_node
            return 
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size+=1
        return

        
    def popfront(self):
        if self.empty():
            return
        self.head = self.head.next
        self.size-=1
            
    def popback(self):
        if self.empty():
            return
        current, current.next = self.tail.prev, None
        self.prev = None
        self.tail = current
        self.size-=1

    def deletekeys(self,val):
        if self.empty():
            return
        node, prev = self.head, None
        if self.size == 1 and self.head.data == val:
            self.head = self.tail = None
            return
        while node:
            if node.data == val:
                if node.prev is None:
                    self.head = self.head.next
                    self.head.prev = None
                elif node.next is None:
                    prev = node.prev
                    prev.next = None
                    node.prev = None
                    self.tail = node
                else:
                    prev = node.prev
                    prev.next = node.next
                    node.next.prev = prev
                self.size-=1
            node = node.next
        print("Successfully deleted the key:",val)
    
    def changekey(self,val,newval):
        if self.empty(): return
        current = self.head
        while current:
            if current.data == val:
                current.data = newval
                break
            current = current.next
        if current is None:
            print(val, "does not exist in the list")
        print("Success:", val, "changed into", newval)
        
    def addlist(self,other):
        if self.empty() and other.empty(): return
        elif self.empty():
            print("this is just other list")
            return other
        elif other.empty():
            print("this is just self list")
            return self
        else:
            newlist2 = doublylinkedlist()
            newlist2.copylist(other)
            newlisttail = newlist2.tail
            self.tail.next = newlist2.head
            self.tail.next.prev = self.tail
            self.tail = newlisttail
            self.size += other.size
            return self
        
    def reverselist(self):
        temp, node = None, self.head
        while node:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev
        if temp:
            self.head = temp.prev
            
    def sorting(self):
        if self.empty(): return
        sortedlist = doublylinkedlist()
        traversed = []
        node = self.head
        while node:
            traversed.append(node.data)
            node = node.next
        traversed.sort()
        for i in traversed:
            sortedlist.lappend(i)
        self.copylist(sortedlist)

    def printlist(self, *args):
        printed = []
        node = self.head
        
        if len(args) == 0:
            if node is None:
                print("The list is empty")
                return
        elif len(args) == 1:
            node = args[0]
        else:
            print("there are too many arguments")
            return
        while node:
            printed.append(str(node.data))
            node = node.next
        print("This list is: {}".format(', '.join(printed)))   
        return
        
    def datalist(self):
        node = self.head
        dlist = []
        while node:
            dlist.append(node.data)
            node = node.next
        return dlist
    
    
    
#Functions out of this DoublyLinkedList
def multijoinedlists(*args):
    numargs = len(args)
    if numargs < 2:
        print("Too few list arguments")
        return
    elif numargs == 2:
        return newcombinedlist(args[0], args[1])
    newlist = doublylinkedlist()
    newlist.copylist(args[0])
    for i in range(1, numargs):
        auxlist = doublylinkedlist()
        auxlist.copylist(args[i])
        newlist.tail.next = auxlist.head
        auxlist.head.prev = newlist.tail
        newlist.tail = auxlist.tail
        newlist.size += auxlist.size
    return newlist
        
def howsimilar(l1,l2):
    node1, node2 = l1.head, l2.head
    
    sdata = []
    data1, data2 = l1.datalist(), l2.datalist()
    simindex = 0.0
    while node1:
        if node1.data == node2.data:
            sdata.append(node1.data)
        node1, node2 = node1.next, node2.next
    if len(sdata) == 0:
        print("There are no shared values")
    else: print("These are shared values", sdata)
    simindex = len(set(data1) & set(data2)) / float(len(set(data1) | set(data2))) * 100
    return str(simindex)+"%"

def newcombinedlist(l1,l2):
    if l1.empty() and l2.empty(): return
    elif l1.empty():
        print("this is just other list2")
        return l2
    elif l2.empty():
        print("this is just other list1")
        return l1
    else:
        newlist1, newlist2 = doublylinkedlist(), doublylinkedlist()
        newlist1.copylist(l1), newlist2.copylist(l2)
        newlist1.tail.next = newlist2.head
        newlist2.head.prev = newlist1.tail
        newlist1.size = (l1.size + l2.size)
        return newlist1
        
def copyfromhead(head):
    current, newList, tail = head, None, None
    while current:
        if newList is None:
            newList = Node(current.data)
            tail = newList
        else:
            tail.next = Node(current.data)
            tail = tail.next
        current = current.next
    return newList

def headprint(node):
    printed = []
    while node:
        printed.append(str(node.data))
        node = node.next
    print("This list is: {}".format(' '.join(printed)))
        
            

        