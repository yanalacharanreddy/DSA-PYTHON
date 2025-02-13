class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.head ==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.prev=self.tail
            self.tail.next=newnode
            self.tail=newnode
            
    def DeletionAtBegin(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None   
    def Display(self):
        temp=self.head
        while temp !=None:
            print(temp.data,end=' ')
            temp=temp.next
        
        
        
dll=DoublyLinkedList()
dll.InsertAtEnd(1)
dll.InsertAtEnd(2)
dll.InsertAtEnd(3)
dll.InsertAtEnd(4)
dll.Display()
print()
dll.DeletionAtBegin()
dll.Display()
