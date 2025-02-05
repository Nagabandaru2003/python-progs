class Student:
    def Cook(self):
        print("Student is cooking")
    
    def play(self):
        print('Student is playing')

class Employee(Student):
    def work(self):
        print("Employee is working")
    def cook(self):
        print('Employee is cooking')
        
e = Employee()
e.play()

'''
work() : Specialized Method : only in child class
play() : Inherited : used it is child class
cook() : Overridden Method: Change Implementation in child
'''