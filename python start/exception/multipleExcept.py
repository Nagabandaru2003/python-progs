def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionErroe occured and Handled')
    except NameError:
        print("NameError occured and Handled")  
    except TypeError:
        print("Type error occured and handled")  
disp(10,0)
disp(10,'kodnest')