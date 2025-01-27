class employee :
    def __init__(self, name, age, designation, company_name):
        self.name = name
        self.age = age
        self.designation = designation
        self.company_name = company_name
    def login(self,time):
        print(f"{self.name},logged out at{time}")
    def hours(self,hours):
        print(f"{self.name} worked for {hours}")
    
    def getDetailes(self):
        print('employee Name: ',self.name)
        print('employee age:',self.age)
        print("employee designation: ",self.designation)
    
 e1 =  employee('ak',24,)