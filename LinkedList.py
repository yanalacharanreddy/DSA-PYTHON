class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.head==None :
            self.head=newnode
        else:
            temp=self.head
            while temp.next != None :
                temp=temp.next
            temp.next=newnode
    def Display(self):
        temp=self.head
        while temp!=None :
            print(temp.data,end=' ')
            temp=temp.next
                        
            

sll=SinglyLinkedList()
sll.InsertAtEnd(1)
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtEnd(4)
sll.Display()