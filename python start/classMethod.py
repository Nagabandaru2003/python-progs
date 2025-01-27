class Student:
    collage_name = "ANNAMACHARYA INSTITUTE OF TECHNOLOGY"
    
    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
        
    @classmethod
    def Ch_collage_name(cls, new_name):
        cls.collage_name = new_name
        
    def attend_class(self):
        print(f"{self.name} from {Student.collage_name} is attending the class.")
        
Student.Ch_collage_name("RGM collage")

st_1 = Student("Naga",21,'220')
st_2 = Student("subbu",25,'420')

st_1.attend_class()
st_2.attend_class()

st_1.Ch_collage_name("srit collage")

print(Student.collage_name)