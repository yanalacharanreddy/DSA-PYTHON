class Human:
     name= "Homo Sapein Sapein"
     def CradleCermony(self,myname):
         self.name=myname
    
h1=Human()
h2=Human()
print(Human.name,h1.name,h2.name)
Human.CradleCermony(h1,"vineeth")
print(h1.name)

