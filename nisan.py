#1.take two number from the user and perform:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("division:",a/b)
print("remainder:",a%b)
print("floor division:",a//b)
print("power:",a**b)

#2.1.program to calculate area and perimeter of rectangle:
l=int(input("enter a value of length:",))
b=int(input("enter a value of breadth:",))
a=print("area of rectangle:",l*b)
p=print("perimeter of rectangle:",2*l+2*b)

#2.2.program to calculate area and perimeter of square:
s=int(input("enter a value of side:",))
print("area of square:",s*s)
print("perimeter of square:",4*s)

#2.3.program to calculate area and circumference of circle:
r=int(input("enter value of radius:",))
print("area of circle:",3.14*r**2)
print("circumference of circle:",2*3.14*r)

#3.average of therr numbers:
a=int(input("enter a number:",))
b=int(input("enter a number:",))
c=int(input("enter a number:",))
d=a+b+c
e=d//2
print("average:",e)

#4.programs to check
#4.1.both numbers are equal
a=int(input("enter a number:",))
b=int(input("enter a number:",))
if a==b:
    print("equal")
else:
    print("not equal")
#4.2.a number is greater than other number:
a=int(input("enter a number:",))
b=int(input("enter a number:",))
if b<a:
    print("a is greater than b")
else:
    print("b is greater than a")
#4.3.to find the number is less than or equal to another number:
a=int(input("enter a number:",))
b=int(input("enter another number;",))
if a<b:
    print("a is less than b")
elif a==b:
    print("the numbers are equal")
else:
    print("b is less than a")

#5.to find the square root of a number:
a=int(input("enter a number:",))
print("the square root of the number is:",a**0.5)

#6.to find simple interest and compound interest of a number:

#7.
x=10
x += 5
x -= 3
x *= 2
x /= 4
x %= 2
x **= 3
print(x)

#8.swapping of two numbers:

#9.to find cube root of a number:
a=int(input("enter a number to find its cube root",))
print(a**0.33)

#10.to find last two digits of 8523:
a=8523
print("the last two digits are",a%100)

#11.to remove last two digits of 8523:
a=8523
print(a//100)
