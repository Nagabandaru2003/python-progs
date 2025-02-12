# def disp():
#     return 10
#     return 20
#     return 30

# res = disp()
# print(res)

def generator_function():
    print('hello')
    yield 10
    yield 20
    yield 30
    
ref = generator_function()

print(next(ref))
print(next(ref))
print(next(ref))
#print(next(ref))
