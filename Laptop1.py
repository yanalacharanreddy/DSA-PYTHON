class Laptop:
    brand='Dell'
    def __init__(self,brand,ram,rom):
        self.brand=brand
        self.ram=ram
        self.rom=rom
    def info(self):
        print(self.brand,self.ram,self.rom)
Lap1=Laptop('Hp','16gb','512gb')
Lap1.info()
print(Laptop.brand,Lap1.brand)
Laptop.brand="Apple Mac"
print(Laptop.brand,Lap1.brand)