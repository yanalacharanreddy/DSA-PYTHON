print("Hello World")
a=5
b=a
print(b)
c=6;d=7
print(c,d)
print(b,c,sep="")
#the above the 'sep' we can remove space b/w the two vars and also can use other symbols to separate them
print(a,end="----")
print(b)
#by using the above 'end' function instead of printing the values in the next line we can print them in the same line
print("%d %d"%(a,c))
# The above is the modulo operator like this also we can print the variables
print("a={} b={}".format(a,c))
print("a={1} b={0}".format(a,c))
print("a={0} b={1}".format(a,c))
# By using the 'format' we can arrange those values as a indexed foramt and we can use those and print via using index
