class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.head == None :
            self.head=newnode
        else :
            newnode.next =self.head
            self.head=newnode
       
    def Display(self):
        temp=self.head
        while temp!=None :
            print(temp.data,end=' ')
            temp=temp.next
                        
            

sll=SinglyLinkedList()
sll.InsertAtBegin(1)
sll.InsertAtBegin(2)
sll.InsertAtBegin(3)
sll.InsertAtBegin(4)
sll.Display()