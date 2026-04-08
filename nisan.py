#take two number from the user and perform:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("division:",a/b)
print("remainder:",a%b)
print("floor division:",a//b)
print("power:",a**b)

#program to calculate area and perimeter of rectangle:
l=int(input("enter a value of length:",))
b=int(input("enter a value of breadth:",))
a=print("area of rectangle:",l*b)
p=print("perimeter of rectangle:",2*l+2*b)

#program to calculate area and perimeter of square:
s=int(input("enter a value of side:",))
print("area of square:",s*s)
print("perimeter of square:",4*s)

#program to calculate area and circumference of circle:
r=int(input("enter value of radius:",))
print("area of circle:",3.14*r**2)
print("circumference of circle:",2*3.14*r)

#average of therr numbers:
a=int(input("enter a number:",))
b=int(input("enter a number:",))
c=int(input("enter a number:",))
d=a+b+c
e=d//2
print("average:",e)

#programs to check
#both numbers are equal
a=int(input("enter a number:",))
b=int(input("enter a number:",))
if a==b:
    print("equal")
else:
    print("not equal")
#a number is greater than other number:
a=int(input("enter a number:",))
b=int(input("enter a number:",))
if b<a:
    print("a is greater than b")
else:
    print("b is greater than a")
    
