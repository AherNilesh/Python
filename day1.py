x=10
print(x)

#program 1
a=19
print(a)

#program 2
#arithmetic operation

b=20
c=10
print(b+c)
print(b-c)
print(b*c)
print(b/c)
print(b%c)
print(24%7)

def Calculator(y,z):
    print(y + z)
    print(y - z)
    print(y * z)
    print(y / z)
    print(y % z)

Calculator(8,4)
Calculator(10,5)

# function without parameter and without return type
def addN():
    print(6+6)
addN()
addN()
addN()


# function with parameter and without return type
def addM(a,b):
   print(a+b)
addM(10,5)
addM(12,3)


# function with parameter and with return type
def addT(d,f):
    return d+f
q1=addT(3,4)
print(q1)
print(q1+q1)

def subD(a,b):
    return a-b
q2=subD(20,11)
print(q2)
