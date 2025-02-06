def disp(a,b):
    try:
        print(a/b) #zeroDivision error
    except:
        print('some error handle')
    

disp(10,0)
disp(10,5)
disp(20,5)

    