class Laptop:
    brand='Dell'  #Class Variable
    def __init__(self,ram,rom):
        
        self.ram=ram  #instance variable 
        self.rom=rom  #instance variable
    def info(self):
        print(self.brand,self.ram,self.rom)
comp1=Laptop('15gb','88gb')
comp2=Laptop('5gb','66gb')
comp1.info()
comp2.info()
print(comp1.brand,comp2.brand,Laptop.brand)
comp1.brand='HP' #changing instance variable
print(comp1.brand,comp2.brand,Laptop.brand)
Laptop.brand='Lenovo' #changing Class Variable
print(comp1.brand,comp2.brand,Laptop.brand)



