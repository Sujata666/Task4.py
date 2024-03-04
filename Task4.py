# calculator 
print("press1. for addition")
print("press2.for subtraction")
print("press3.for multiplication")
print("press4.for division")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
s=int(input("enter the choice:")) 
match s:
 case 1:
  m=a+b
  print("the addition of the number is",m)
 case 2:
  m=a-b
  print("the subtraction of the number is",m)
 case 3: 
  m=a*b

  print("the multiplication of the number is",m)
 case 4:
  m=a/b
  print("the division of the number is ", m)
