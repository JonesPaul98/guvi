#Perimeter of rectangle-While loop
i=1
n=int(input("enter the range:"))
while i<=n:
  l=int(input("enter the length:"))
  b=int(input("enter the breadth:"))
  perimeter=2*(l+b)
  i=i+1
  print("Perimeter of rectangle:",perimeter)
  
#area of rectangle-While loop
i=1
n=int(input("enter the range:"))
while i<=n:
  l=int(input("enter the length:"))
  b=int(input("enter the breadth:"))
  area=(l*b)
  i=i+1
  print("area of rectangle:",area)

  # circle operation-While loop
  i=1
n=int(input("enter the range:"))
while i<=n:
  r=int(input("enter the radius:"))
  circumference=2*3.14*r
  area=3.14*r*r
  diameter=2*r
  i=i+1
  print("area of circle:",area)
  print("area of circle:",circumference)
  print("area of circle:",diameter)
