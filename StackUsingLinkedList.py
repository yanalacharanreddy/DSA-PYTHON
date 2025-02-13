class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class Stack:
    capacity = 5
    top = 0
    def __init__(self):
        self.Head = None 
    
    def PUSH(self, data):
        newnode = Node(data)
        if self.top<self.capacity:
            print(newnode.data," is Pushed into stack")
            newnode.next = self.Head
            self.Head = newnode
            self.top += 1 
        else:
            print("Stack Overflow")
        
    def POP(self):
        if self.top>0:
            print(self.Head.data," is Popped from stack")
            self.Head = self.Head.next
            self.top -= 1 
        else:
            print("Stack Underflow")
            
    def PEEK(self):
        if self.top>0:
            print(self.Head.data," is top element in stack")
        else:
            print("stack is Empty")
            
    
    def Display(self):
        if self.top<=0:
            print("Stack is Empty")
        else:
            print("Stack:- ",end='')
            temp = self.Head
            while temp:
                print(temp.data,end=' ')
                temp = temp.next 
            print()

if __name__ == "__main__":
    stk = Stack()

    print("\n**********WELCOME TO STACK OPERATIONS***********")
    print("Enter 1 to PUSH an element into Stack")
    print("Enter 2 to POP an element from Stack")
    print("Enter 3 to PEEK into Stack")
    print("Enter 4 to Display all elements in Stack")
    print("Enter -1 to EXIT\n")
    
    while(True):
        ip = int(input("Enter your Choice :-  "))
        if ip==1:
            data = int(input("Enter your push value :- "))
            stk.PUSH(data)
        elif ip==2:
            stk.POP()
        elif ip==3:
            stk.PEEK()
        elif ip==4:
            stk.Display()
        elif ip==-1:
            print("You have Exited the Program")
            break
        else:
            print("Invalid Choice ")
        