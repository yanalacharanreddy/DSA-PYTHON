class Computer:
    def __init__(self,brand,ram,rom):
        self.brand=brand
        self.ram=ram
        self.rom=rom
    def info(self):
        print(self.brand,self.ram,self.rom)
comp1=Computer('Dell','15gb','88gb')
comp2=Computer('Hp','5gb','66gb')
print(comp1.info)
print(comp2.info)
