# Encapsulation is hiding actual implimentaion
# Abstraction means provide access to encapsulated attributes and behaviour without knowing their actual implimentation
# for ex. when we append value to list using .append() method, it is get added to the end of sequence. 
    # Here append method is layer of abstraction and its implementation encapsulated inside List class  
# Polymorphism is a process of providing abitity to have many forms. 
# ex. method overriding, operator overloading
# Inheritance is proccess of having access to attributes and behaviours of base class within derived class
# types- Single, multiple, multilevel, hybrid4




# Learning points:
# - Abstract class and methods.
# - ABC and abstractmethod
# Method Resolution Order
# method overriding
# operator overloading
# super()



from abc import ABC, abstractmethod


class TestAbstractClass(ABC):

    def __init__(self):
        pass

    @abstractmethod    
    def first(self):
        print('first')
        pass

    @abstractmethod     
    def second(self):
        pass

    @abstractmethod     
    def third(self):
        pass


class TestClassOne(TestAbstractClass):

    def first(self):
        print('first')
        pass
   
    def second(self):
        pass
  
    def third(self):
        pass



c = TestClassOne()
c.first()