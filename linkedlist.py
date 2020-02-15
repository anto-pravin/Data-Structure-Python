class node(object):
  def __init__(self,data):
    self.data = data
    self.next = None

class linkedlist(node):
  
  def __init__(self):
    self.head = None
  
  
  def insertfirst(self,data):
    newnode = node(data)
    if not self.head:
        self.head = newnode
    else:
        newnode.next = self.head
        self.head = newnode

  def insertlast(self, data):
      newnode = node(data)
      actualnode = self.head
      if self.head is None:
          self.insertfirst(data)
      else:
          while actualnode.next is not None:
              actualnode = actualnode.next
          actualnode.next = newnode
  def remove(self, index):
      self.count = index
      actualnode = self.head
      i = 0
      while i != self.count-1:
          previousnode = actualnode
          actualnode = actualnode.next
          i+=1
      previousnode.next = actualnode.next



  def disp(self):
    l=[]
    actualnode = self.head
    while actualnode is not None:
      l.append(actualnode.data)
      actualnode = actualnode.next
    return l


a = linkedlist()
n = int(input())
l = list(map(int,input().split()))
for i in range(n):
  a.insertlast(l[i])
if n%2 == 0:
    a.remove(n//2)
else:
    a.remove(n//2+1)
print(*a.disp())