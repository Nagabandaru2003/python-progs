# li = [10,20,30,40,50]
# print(type(li))
# iterator_object = iter(li)
# print(type(iterator_object), iterator_object)

# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))
# print(next(iterator_object))

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        print(a)
        a,b = b, a+b
        
fibonacci(10)


def fibonacci_gen(num):
    a,b = 0,1
    for i 
    