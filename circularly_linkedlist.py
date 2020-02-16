#This program will get a list and right-rotate the list

class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class circularly_linkedlist(node):
    def __init__(self):
        self.head = None

    def insertfirst(self, data):
        newnode = node(data)
        if not self.head:
            self.head = newnode
            newnode.next = self.head

        else:
            newnode.next = self.head
            self.head = newnode

    def insertlast(self, data):
        newnode = node(data)
        if not self.head:
            self.insertfirst(data)
        else:
            actualnode = self.head
            while actualnode.next is not self.head:
                actualnode = actualnode.next
            actualnode.next = newnode
            newnode.next = self.head

    def insert(self, data):
        self.insertlast(data)

    def disp(self):
        actualnode = self.head
        l = []
        while actualnode.next is not self.head:
            l.append(actualnode.data)
            actualnode = actualnode.next
        l.append(actualnode.data)
        return l

    def shift(self, data):
        actualnode = self.head
        l = []
        for  i in range(data):
            actualnode = actualnode.next
        stop = actualnode
        while stop.next is not actualnode:
            l.append(stop.data)
            stop = stop.next
        l.append(stop.data)
        return l


n = int(input())
k = list(map(int,input().split()))
s = int(input())
a = circularly_linkedlist()
for i in k:
    a.insert(i)
print(*a.shift(s))
