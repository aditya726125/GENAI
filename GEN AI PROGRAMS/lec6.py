#function-- perform some action
#1--built in functions- len() , print() , type()
#2--User defined functions- defined by users according to the need 
#syntax -- { def function_name():
#              code to be executed }

#user defined function without argument
from turtle import width


def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number:")) 
    return a+b
print(add())

#positional argument-- These argument defined during the function and put the value of argument during call the function
def Calculation(a, b):
    print("addition: " ,a+b)
    print("Subtraction:", a-b)
    print("Multiplication:", a*b)
    print("division:", a/b)
    return"Calculation is complete"
print(Calculation(10,5))

#default argument--
def area_perimeter(width = 8 , height =7):
area = width*height # type: ignore
perimeter = 2*(width+ height) # pyright: ignore[reportUndefinedVariable]
return " Area is", area, "and perimeter is, perimeter"
print(area_perimeter(10))

#keyword argument
def interest(p, r, t):
    i = (p*r*t)/100
    return i
print(interest(t=2, p = 1000, r = 10))

#mixed argument-- positional+keyword argument(positional argument follows keyword argument)
print(interest(1000, t=2, r=10))

#positional variable length argument -- 
#variable length argument-- we give multiple number of input to a function.
#1. Non-keyword variable length argument        2. keyword variable length argument
#it is behave as tuple,represent by star(*)        #it is behave as dictionary, represent by double star(**)

#non-keyword variable length argument
def test(*args):
    print(args)
    print(len(args))
    print(type(args))
test(6, 8 ,3, 9, 8)

def sum_number(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(sum_number(66,90,27,27))

#keyword variable length argument
def test(**kwargs):
    print(kwargs)
    print(len(kwargs))
    print(type(kwargs))
    test(a=7, b=3 )