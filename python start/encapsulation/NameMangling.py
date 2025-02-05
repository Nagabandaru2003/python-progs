class Demo1:
    def __init__(self,name):
        self.__name = name   #Private Variable
   

d1 = Demo1('Akash')
#print(d1.__name)#Error
print(d1._Demo1__name)

#print(d1.name) #Error


'''
1.NameMangling is the process of providing new name to the private variable.
2.these new names will be provided automatically by python
for all private members.

3.New name will be provided in format:
objectName._className__VariableName
'''