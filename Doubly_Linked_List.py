# rotation of the list using doubly_linked list
''' Input :
            6
            1 2 3 4 5 6
            4
    Output :
            3 4 5 6 1 2    '''

class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doubly_linkedlist(node):
    def __init__(self):
        self.head = None
        self.tail = None

    def insertfirst(self,data):
        newnode = node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            newnode.previous = self.head

    def insertlast(self, data):
        newnode = node(data)
        if not self.tail:
            self.insertfirst(data)
        else:
            newnode.previous = self.tail
            self.tail.next = newnode
            self.tail = newnode

    def pop(self):
        newnode = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        del(newnode)

    def rotate(self,key): #key is the number of times the list has to be rotated
        for i in range(key):
            self.insertfirst(self.tail.data)
            self.pop()

    
    def traverse(self): # Returns the answer
        answer = []
        actualnode = self.head
        while actualnode is not None:
            answer.append(actualnode.data)
            actualnode = actualnode.next
        return answer

a = doubly_linkedlist()
size = int(input()) # Size of the array
List = list(map(int,input().split()))
key = int(input())
for i in List:
    a.insertlast(i)
a.rotate(key)
print(*a.traverse())      