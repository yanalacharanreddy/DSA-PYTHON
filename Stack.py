def PUSH(data):
    if len(stack)<capacity:
        stack.append(data)
        print(data," is pushed into stack")
    else:
        print("Stack Overflow")

def POP():
    if stack:#len(stack)>0
        print(stack[-1]," Popped from stack")
        stack.pop()
    else:
        print("Stack Underflow")
        
        
def PEEK():
    if stack:
        print(stack[-1])
    else:
        print("Stack is Empty")
    
def Display():
    if stack:
        print(stack)
    else:
        print("stack is Empty")

if __name__ == "__main__":
    stack = []
    
    capacity = int(input("Enter Stack capacity:- "))
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
            PUSH(data)
        elif ip==2:
            POP()
        elif ip==3:
            PEEK()
        elif ip==4:
            Display()
        elif ip==-1:
            print("You have Exited the Program")
            break
        else:
            print("Invalid Choice ")