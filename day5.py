#program
a1=" jaipur "
print(len(a1))

a2=a1.strip()
print(a2)
print(len(a2))

#program
info="nilesh s aher"
a3=info.split(" ")
print(a3)
print(type(a3))

#program 3
email="nilesh@gmail.com"
a4=email.split('@')
print(type(a4))
print(a4)

#progra, 4
info2= "I am learning javascript"
a5 = info2.replace("javascript","python")
print(a5)

#program 5
num= "14"
a5=num.isdigit()
print(a5)

#program 6
num2 = "adasdsa"
a6 = num2.isalpha()
print(a6)

num3 = "A213213 "
a7 = num3.isalnum()
print(a7)

#program 8

b1 = " goa "
print(len(b1))
z1 = b1.strip()
print(len(z1))

# program 9
b2 = " Bhopal"
q2 = b2.lstrip()
print(len(q2))

# program 10
b3 = " wardha "
print(len(b3))
z3 = b3.rstrip()
print(len(z3))

# program 11
info3="I am learning js "
z4=info3.title()
print(z4)

#PROGRAM 12

p1="pune is nice place"
s1=p1.capitalize()
print(s1)

# program 13
city10 = "NaGpur"
s2 = city10.swapcase()
print(s2)


city11 = "chandrapuraea"
s3= city11.index("a",5)
print(s3)

s4 = city11.index("a",7,11)
print(s4)

city12 = "chandrapuraea"
q8 = city12.index("a",5)
print(q8)

q9 = city12.index("a",7,11)
print(q9)

