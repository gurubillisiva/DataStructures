class Node:
  def __init__(self,data):
    self.data=data
    self.nextt=None

class SLL:
  def __init__(self):
    self.head=None

  def insertAtBeg(self,data):
    temp=Node(data)
    temp.nextt=self.head
    self.head=temp
  
  def delAtBeg(self):
    temp=self.head
    self.head=self.head.nextt
    temp.nextt=None

  
  def printList(self):
    temp=self.head
    while temp!=None:
      print(temp.data,"==>",end='')
      temp=temp.nextt
    print("None")

obj=SLL()
ch=0
while ch!=4:
  print("Linked list implementation\n","1.Insertion at begining 2. Deletion 3. Print Llist 4. Exit")

  ch=int(input())
  

  if ch==1:
    print("enter value of the node")
    data=input()
    obj.insertAtBeg(data)
    obj.printList()
  elif ch==2:
    obj.delAtBeg()
    obj.printList()
    
  elif ch==3:
    obj.printList()
    
    
  
