from Kethuavadahinh import *
class Student(Person):
    def __init__(self,name,age,email,university):
        super().__init__(name,age,email)
        self.university = university
    def info(self):
        print(self.age)
at = Student("SV1",19,"Admin@gmail.com","ĐH Ngoại thương")
at.info()

class Animal():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight =weight
    def info(self):
        print('Class Animal: info()')

class Film():
    def __init__(self,author,year,type):
        self.author = author
        self.year =year
        self.type = type
    def info(self):
        print('Class Film: info()')
    def show_author(self):
        print('Author: ',self.author)

class Mouse(Animal,Film):
    def __init__(self,name,age,weight,author,year,type):
        Animal.__init__(Animal,name,age,weight)
        Film.__init__(Film,author,year,type)
mouse = Mouse('Micky',12,10,'walt Desneey',1997,'Cartoon')
mouse.info()
print(mouse.weight)
mouse.show_author()