class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.head ==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def Display(self):
        temp=self.head
        while temp !=None:
            print(temp.data,end=' ')
            temp=temp.next
        
        
        
dll=DoublyLinkedList()
dll.InsertAtBegin(1)
dll.InsertAtBegin(2)
dll.InsertAtBegin(3)
dll.InsertAtBegin(4)

dll.Display()