# -*- coding: utf-8 -*-
"""
Created on Sun May  1 04:28:32 2022

@author: ******* NU
"""

class Node:
    
    
    def __init__(self,data):
        self.data = data
        self.position = 0
        self.next = None
        
class singlyLinkedList:
    
    def __init__(self):
        self.head = None
        self.end = None
        self.count = 0
    
    def append(self,data):
        
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.count += 1
            self.end = self.head
            new_node.position = self.count
            return True
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            end = curr.next
            self.count += 1
            new_node.position = self.count
            return True
        return False
            
    def length(self):
        return self.count
    
    def search(self,search_data):
        
        curr = self.head
        if self.head == None:
            return True
        else:
            while curr != None:
                if curr.data == search_data:
                    return True
                curr = curr.next
        return False
    
    def insert(self,insert_data,pos):
        
        new_node = Node(insert_data)
        curr = self.head
        prev = None
        if self.head == None: 
            self.head = new_node
            self.count += 1
            self.end = self.head
            new_node.position = self.count
            return True
        else:
            while curr != None and curr.position < pos:
                prev = curr
                curr = curr.next 
            prev.next = new_node
            new_node.next = curr
            new_node.position = pos
            self.count += 1
            while curr != None:
                curr.position += 1
                curr = curr.next
            return True
        return False
                
    def deleteBegin(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            return
   
    def deleteEnd(self):
        
        if self.head == None:
            return True
        else:
            curr = self.head 
            prev = None
            while curr.next != None:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            return True
        return False
    def printList(self):
        
        if self.head == None:
            print('List is empty')
        else:
            curr = self.head
            while curr != None:
                print('the data is {} and position is {}'.format(curr.data,curr.position))
                curr = curr.next
    
def main():
    lists = singlyLinkedList()
    lists.append(1)
    lists.append(3)
    lists.append(2)
    lists.insert(10, 2)
    lists.printList()
    print(lists.count)

if __name__ == "__main__":
    main()
            
                
    
