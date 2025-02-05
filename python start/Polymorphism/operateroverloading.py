class Demo1:

    def __str__(self):
        return 'Hello'
    def __add__(self,other):
        self.a = 20
        other.b = 30
        return self.a + other.b
        

class Demo2:
    def __str__(self):
        return 'Hi'
        
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
print(d1+d2)

'''
In Python if we print reference variable then internally python
will invoke str () which always return string representation of an 
address of an object. 

In the above examples we have overridden __str__ methods in their
respective classes.
'''

'''
Dunder methods : The methods which has suffix and prefis as - 
these dunder methids can be called as magic methods because as programmer
we no need to call any 
'''