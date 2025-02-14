def Enqueue(data):
    global front
    global rare
    if front ==-1 and rare==-1:
        queue.append(data)
        front=0
        rare=0
        print(queue[rare],"is Enqueued into queue")
        
    else:
        rare+=1
        queue.append(data)
        print(queue[rare],"is Enqueued into queue")
        
def Dequeue():
    global front
    global rare
    if front==-1 and rare==-1:
        print("Queue is empty")
    elif front==0 and rare==0:
        print(queue[front],"id Dequeued from queue")
        queue.pop(0)
        front =-1
        rare =-1
    else:
        print(queue[front],"is Dequeued from queue")
        queue.pop(0)
        rare-=1
        

def Display():
    if queue:
        print(queue)
    else:
        print("queue is empty")
        
if __name__== "__main__":
    queue=[]
    front=-1
    rare=-1
    
    print("\n *******Welcome to Queue Operations *******")
    print("Enter 1 to Enqueue the element into the queue")
    print("Enter 2 to Dequeue the element from the queue")
    print("Enter 3 to Display all the elements in the queue")
    print("Enter -1 to EXIT\n")
    
    while(True):
        ip=int(input("Enter your choice:-"))
        if ip==1:
            data=int(input("Enter the value "))
            Enqueue(data)
        elif ip==2:
            Dequeue()
        elif ip==3:
            Display()
        elif ip==-1:
            print("You have exited the program")
            break
        else:
            print("Invalid Choice")
    