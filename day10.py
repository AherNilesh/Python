dict1={
    "firstname":"nilesh",
    "lastname":"aher",
    "age":21,
    "rollno":1
}
print(type(dict1))
dict2=dict1
dict2['firstname']="rahul"
print(dict2)
print(dict1)


vehicle = {
        "color":"blue",
        "city":"pune",
        "regNo":1234
}
print(vehicle)
vehicle2=vehicle.copy()
vehicle2['color']="red"
print(vehicle2)
print(vehicle)


#program 3

vehicle3 = {
        "color":"blue",
        "city":"pune",
        "regNo":1234
}
#program 4

#pop--remove
print(vehicle3.pop('color'))
print(vehicle3)

#program 5
a=vehicle3.get('type')
print(a)

#program 6

dict2={
    "firstname":"nilesh",
    "lastname":"aher",
    "age":21,
    "rollno":1
}
for x in dict2:
    print(x,dict2[x])

for prop in dict2.keys():
    print(prop)

for val in dict2.values():
    print(val)

for item in dict2.items():
    print(item)

#dict2.clear()
#print(dict2)

#fromkey()
a = ("name","age","rollNo")
b = None
q1 = dict.fromkeys(a,b)
print(q1)





