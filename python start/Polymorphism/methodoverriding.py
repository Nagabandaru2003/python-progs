class Calculator:
     def calculate(self,a,b):
         pass
class Add(Calculator):
    def calculate(self,a,b):
        print('Addition:',a+b)
    
class Sub(Calculator):
    def calculate(self,a,b):
        print('Subtraction:',a-b)

class Mul(Calculator):
    pass

ref = Add(10,20)
ref.calculate()

ref = Sub()
ref.calculate(20,10)

ref Mul()

        
