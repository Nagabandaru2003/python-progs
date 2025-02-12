def decor(func):
    def inner(name):
        if name == "naga":
            print(name ,"is learning JAVA")
        else:
            func(name)
    return inner

@decor
def choice(name):
    print(name,"Is learning Python")
    
choice('naga')
choice('naga')