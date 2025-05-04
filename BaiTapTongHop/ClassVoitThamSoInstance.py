'''
Dinh nghia mot lop gom co tham so lop va co cung tham so instance
'''

class Person:
    name = "An Mun"

    def __init__(self, name = None):
        self.name = name

# Du lieu vao
student1 = Person("Nguyet")
print(Person.name + ' name la '+ student1.name)
student2 = Person()
student2.name = "Nguyet nha"
print(Person.name + ' name la '+ student2.name)
