class node(object):
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.previous = None

class doubly_linkedlist(node):
    def __init__ (self):
        self.head = None
        self.tail = None

    def insertfirst(self, data):
        newnode = node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.previous = newnode
            self.head = newnode

    def insertlast(self, data):
        newnode = node(data)
        if not self.head:
            self.insertfirst(data)
        else:
            actualnode = self.head
            while actualnode.next is not None:
                actualnode = actualnode.next
            actualnode.next = newnode
            newnode.previous = actualnode
            self.tail = newnode

    def traverse(self):
        actualnode = self.head
        l = []
        while actualnode is not None:
            l.append(actualnode.data)
            actualnode = actualnode.next
        return l

    def add(self):
        actualnode = self.tail
        if actualnode.data == 9:
            while actualnode.data == 9:
                actualnode.data = 0
                if actualnode.previous is None:
                    newnode = node(1)
                    newnode.next = actualnode
                    actualnode.previous = newnode
                    actualnode = actualnode.previous
                else:
                    actualnode = actualnode.previous

            actualnode.data += 1
        else:
            actualnode.data += 1


    def check(self):
        firstnode = self.head
        lastnode = self.tail
        while firstnode.next != lastnode.previous:
            if firstnode.data == lastnode.data:
                
                firstnode = firstnode.next
                lastnode = lastnode.previous
            else:
                return 'no'
        return 'yes'


    def traverse_reverse(self):
        actualnode = self.tail
        l = []
        while actualnode is not None:
            l.append(actualnode.data)
            actualnode = actualnode.previous
        return l

n = int(input())
l = list(input())
a = doubly_linkedlist()
for i in l:
    a.insertlast(i)
print(a.check())