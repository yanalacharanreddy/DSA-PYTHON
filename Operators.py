#types of Operators
#1.ARITHMATIC, 2.RELATIONAL, 3.ASSIGNMENT , 4.LOGICAL, 5.BITWISE LOGICAL, 6.IDENTITY

#1.ARITHMATIC
a=5;b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)#division
print(a//b)#Floor Division
print(a%b)#modulo division
print(a**b)#square
print("---------------------------")
      
#2.RELATIONAL
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print("---------------------------")

#3.ASSIGNMENT

a+=b;print(a)
a-=b;print(a)
a*=b;print(a)
a/=b;print(a)
a//=b;print(a)
a**=b;print(a)
a%=b;print(a)
print("---------------------------")
#short hand operators
a=4;
a&=b;print(a)
a|=b;print(a)
a^=b;print(a)

print("---------------------------")

#4.LOGICAL OPERATORS
#shortcircuit operators
print(True and True , True or True)
print(True and False , True or False)
print(False and True , False or True)
print(False and False , False or False)
print(not True, not False)

print(5>2 and 5<8)
print(5>2 and 5<3)
print("---------------------------")

#if we want to compare a and b with variable names then we can use 'is'
#else for variable and literal means we need to use '=='
print (a is b)
print(a is not b)
#MEMBERSHIP OPERATOR
print(1 in [1,2,3,4])
print(5 not in [1,2,3,4])
print("---------------------------")

#BITWISE OPERATORS
print(10 & 7)
print(10|7)
print(10^7)
print("---------------------------")
print(8<<1) #leftshift
print(8>>1) #rightshift
print("---------------------------")
print(223>>3) #a>>b -> a/2**b
print(628<<2) #a<<b -> a*2**b


