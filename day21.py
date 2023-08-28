#lamda
def add(x,y):
    print(x+y)
add(20,5)

# lamda arguments : expression
x=lambda a:a+11
print(x(5))

#prog 2
y=lambda a,b:a*b
a=y(15,9)
print(a)


#progr 3
b=lambda a,b,c:a+b+c
print(b(11,22,33))

#progr 4
def myfunc():
    return lambda a,b:a*b
x=myfunc()
print(x(22,3))

#progr 5
x=lambda a,b:a+b
def myfunc2(n):
    print(n(44,6))
myfunc2(x)

#progr 6

