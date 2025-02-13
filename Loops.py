#For loop is used only when you know the exact no of iteratons

#WAP to print n natural numbers

n=int(input())


for i in range(1,n+1):
     print(i,end=" ")



# while loop is used only when dont know the exact no of iterations

 #WAP to find no of digits in a given number

#Method 1

if(n<0):
    n=n*-1
count=0
while(n>0):
    n=n//10
    count+=1
print(count)

#method 1

a = input()

if a[0]=='-':
    print(len(a)-1)
else:
    print(len(a))
