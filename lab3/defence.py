class Person ():
    def __init__(self, name, age):
        self.name=name
        self.age=age
x=Person("Aynel", 19)
class Student (Person):
    def __init__ (self, name, age, id):
        self.id=id
a=Student("Aynel", 19, 3423)
