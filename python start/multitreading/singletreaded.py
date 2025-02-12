import time
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    for i in li1:
        print(i)
        time.sleep(1)
        
def displayLetter(li2):
    for i in li2:
        print(i)
        time.sleep(1)
    
dd = displayDigits(li1)
dl = displayLetter(li2)