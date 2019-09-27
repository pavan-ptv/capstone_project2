'''capstone project 2 in python'''
import math
VALUE = math.e
print(VALUE)
print("we are printing the e upto the decimal place you want")


def rounde():
    ''' printing the e value upto given decimal places'''
    place = int(input("enter the limit of decimal value:"))
    if place in range(0,16):
        print('your required value of e is:', round(VALUE, place))
    else:
        print("e has only 15 decimal places")


rounde()
