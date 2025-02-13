#WAP to find sum of digits in a given number
n=int(input())
tot=0
while(n>0):
    tot+=n%10
    n=n//10
print(tot)
    
    
