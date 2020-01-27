import random
m={}
userid=random.randint(0,11)
print(userid)
username=(input("enter your name:\n"))
emailid=(input("enter emailid:\n"))
password=(input("enter password:\n"))
k=[username,emailid,password]
m.update({userid:k})
print(m)
j=int(input("Enter the userid:\n"))
g=(input("enter password:\n"))
if j in m.keys():
  if g in k[2]:
    print("Login successful\n")
  else:
    print("Login failure\n")
