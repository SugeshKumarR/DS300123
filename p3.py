class Student:
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    def totalObtained(self):
        return  (self.phy+self.chem+self.bio)

    def percentage(self):
        total = self.totalObtained()
        total= (total/300) * 100
        return total

obj = Student('Mark',70,92,90)
print(obj.percentage())