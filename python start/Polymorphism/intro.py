class Calculator:
    def calculate(self,a,b):
        print('claculate res of a and b')

class Add(Calculator):
    def calculate(self, a, b):
        print("ADDITION: ",a+b)
        
class Sub(Calculator):
    def calculate(self, a, b):
        print("suntraction: ",a-b)
        
def permit(ref,a,b):
    ref.calculate(a,b)
permit(Add(),10,20)
permit(Sub(),20,10)

