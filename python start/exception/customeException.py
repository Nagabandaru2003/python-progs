class PinError(Exception):
    pass
correctPin = 1212
pin = int(input())
try:
    if(pin==correctPin):
        print('Account unlocked')
    else:
        raise PinError('Entered Pin is',pin)
except PinError as e:
    print('Incorrect pin: ',e)
    
