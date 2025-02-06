def checkAge(age):
    if(age<18):
        raise ValueError('Age must be greather than 18')
    
try:
    checkAge(12)
except ValueError as e:
    print("error message:",e)