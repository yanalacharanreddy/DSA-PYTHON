t=()
print(t)
t=(1,2,3,4)
print(t)


l= tuple(map(int,(input().split())))  #to take input as tuple or list from user we do like this
print(l)

a=1,2,3 #by default it becomes a tuple
print(a,type(a))

b=[1,2,3,4,5,6,7,8,9]
print(b[3:6])
print(b[:])
print(b[3:])
print(b[:6])

print(b[::1])
print(b[::2])
print(b[::3])
print(b[::4])

#reverse Slicing

print(b[::-1])
print(b[2:7:-1])
print(b[7:2:-2])
