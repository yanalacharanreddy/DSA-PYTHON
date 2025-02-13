dic={1:"monday",2:5,3:"friday",4:8.5}
print(dic,type(dic))

dic={1:(2,4,5),"name":"Vineeth",4:[5,7]}
print(dic)

d={}
print(d)
d[1]='vineeth'
print(d)
d[2]='ashok'
print(d)
d[3]='bhanu'
print(d)

d=[(1,'a'),(2,'b'),(3,'c')]
print(d)

keys=[1,2,3,4]
values=['a','b','c','d']
d={}

for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

