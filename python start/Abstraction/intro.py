# class Shape:
#     def __init__(self,name):
#         self.name = name
#     def area(self):
#         print('logic to calculate area')

# class Circle(Shape):
#     def __init__(self,name):
#         super().__init__(name)
        
# c1 = Circle('Circle')
# c1.area() 

from abc import ABC, abstractmethod
class Demo1(ABC):
    @abstractmethod
    def disp1(self):
        print('Inside disp1')
        
d1 = Demo1()



'''
If abstract class doesnt have any method then object
for that abstract class can be created
'''

class Demo2(ABC):
    def disp2(self):
        print('Inside disp2')
        
d2 = Demo2()
d2.disp2()



'''
If abstract class  have only concrete method then object
for that abstract class can be created and concrete methods can be invoked.
'''

class Demo3:
    @abstractmethod
    def disp3(self):
        