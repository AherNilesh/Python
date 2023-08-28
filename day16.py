fruit=["apple","mango","banana"]
print(type(fruit))

fruit=("apple","mango","banana")
print(type(fruit))

fruit  = list(fruit)
fruit[1]="chikoo"
fruit = tuple(fruit)
print(fruit)

fruit  = list(fruit)
fruit.append("mango")
fruit = tuple(fruit)
print(fruit)

names  = ("nilesh","poorva","ram","radha")
print(type(names))
print(names[:3])
print(names[1:])
print(names[1:3])


names1= ("nilesh","poorva","ram","radha")

for items in names1:
    print(items)

for item in range(len(names1)):
    print(names1[item])

names1 = list(names)
names1.remove("ram")
print(names1)
names1 = tuple(names1)
print(names1)

#int
j =200
print(j)
print(type(j))

#tuple
j = 110,
print(type(j))

# unpacking
cities=("pune","mumbai","kolkalata","delhi")
a =cities[0]
b =cities[1]
c =cities[2]
d =cities[3]
print(a,b,c,d)

(x1,x2,*x3) = cities
print(x1,x2,x3)

tupleD = (11,22,33)
tupleC = (44,55,66)

tupleE =#tupleD+tupleC
print(tupleE)

t = tupleE * 2
print(t)


