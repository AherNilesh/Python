info=["nilesh","aher",11,55]
print(type(info))

#program-1
dirinfo1={
    "firstname":"nilesh",
    "lastname":"aher",
    "age":21,
    "rollno":1


}
print(dirinfo1)
print(type(dirinfo1))

#program 2
list1=["apple","mango","banana","grapes"]
print(list1)
print(len(list1))

vehicle = {
    "color":"blue",
    "type":"sedane",
    "color":["yellow", "red"]
}
print(vehicle)
print(type(vehicle))

#program 3
animal={
    "name":"lion",
    "legs":4,
    "found":["india","bangaladesh"]
}
q1=len(animal)
print(q1)

#program 4
a=[11,22,33]
print(a[1])

mh = {
    "city1":"delhi",
    "city2":"mumbai"
}
print(mh['city1'])

#add
mh['city3']="pune"

#update
mh['city2']="jaipur"
print(mh)

#delete
del mh['city2']
print(mh)

#prog 5
bank={
    "accno":12345,
    "bal":5000000,
    "branch":"swargate",
    "city":"pune"

}
#retrive
print(bank["accno"])

#add
bank["pincode"] = 411005
print(bank)

#udpate
bank['accno'] = 67890
print(bank)

#del
del bank['city']
print(bank)

#program 6
fruit=["apple","banana","mango","papaya"]

for fr in fruit:
    print(fr)

