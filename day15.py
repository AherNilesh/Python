#program 1
fruits=["apple","mango","banana"]  #list
print(type(fruits))
fruits[2]="grapes"

fruits1=("apple","mango","banana")
print(fruits1)
print(type(fruits1))

# tuple is  fixed  length
# tuple can store duplicate values

vegetable=("carrot","cauliflower","cabbage","cabbage")
print(vegetable[0])
print(vegetable[1])


#vegetable[1] = "ladyfinger"
#print(vegetable)

numberTuple =(11,22,33,44,55)
listTuple =([11,22],[22,33],[44,55])
dictTuple = (
    {"firstName":"nilesh","lastName":"aher"},
    {"firstName":"ram", "lastName":"pansare"}
)
print(type(dictTuple))

#program 2
country =("india","pakistan","srilanka")
print(country[1])
print(country[-1])

# tupleName[startIndex:endIndex (not inclusive)]
print(country[1:])
print(country[:3])
print(country[1:2])
print(country[-3:2])

print("india" in country)
print("India" not in country)

if("india" in country):
    print("name exist")
else:
    print("does not exist")


tupleA =(11,22)
tupleB =(33,44)
tupleC =tupleA+tupleB
print(tupleC)
tupleD = tupleA*4
print(tupleD)


# remove item
state =("MH","MP","UP","RJ")
print(type(state))
state=list(state)
print(state)
state.remove("MP")
print(state)

state = tuple(state)
print(state)
print(len(state))

del state



# program 3 unpackng
tupleA=("rahul","nil","ganesh")

a =tupleA[0]
print(a)
b =tupleA[1]
print(b)
c =tupleA[2]
print(c)

(x1,x2,x3)= tupleA
print(x1)
print(x2)
print(x3)


color=("red","yellow","green","white")
(*c1,c2,c3)=color
print(c1)
print(c2)
print(c3)

color1=("red","yellow","green","white")
for item in color1:
    print(item)



#method
colors1=("red","white","yellow","blue","red")
x1=colors1.count("red")
print(x1)

x2 = colors1.index("yellow")
print(x2)

