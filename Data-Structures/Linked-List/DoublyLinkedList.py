from hmac import new


class Node:

    def __init__(self,prev,next, data):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.count = 0


    def isEmpty(self):
        return self.count == 0

    def appendAtEnd(self,data): 
        newNode = Node(None, None, data)
        if (self.isEmpty()):
            self.head = newNode
            self.end = newNode
            self.count += 1
        else:
            self.end = newNode
            newNode.prev = self.end
            self.end = newNode
            self.count += 1

    def insertSorted(self,data):
        newNode = Node(None, None, data)
        if(self.isEmpty()):
            self.head = newNode
            self.end = newNode
            self.count += 1
        else:
            if self.head.data >= data:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            curr = self.head
            while (curr != None and curr.data < data ):
                curr = curr.next
            


    #def insertBefore(self,data):

    #def insertAfter(self,data):