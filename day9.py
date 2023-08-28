#program 1
list1=["nil","nitin","mukesh"]

#add
list1.append("rahul")
print(list1)
#retrive
print(list1[1])
#remove
list1.pop(1)
#update
list1[2]="avi"
print(list1)

#program 2

dict1={
    "firstname":"nilesh",
    "lastname":"aher",
    "age":21,
    "rollno":1


}
print(type(dict1))
# retrive
print(dict1['firstname'])

# update
dict1['firstname'] = "tanmay"
print(dict1)

# add
dict1['city'] ="mumbai"
print(dict1)

# delete
del dict1['lastname']
print(dict1)

#loop
country=["india","pakistan","china"]

#normal
for city in country:
    print(city)

for city in range(len(country)):
    print(country[city])

dict2 = {
    "fullName":"nilesh aher",
    "skills":["python","java"],
    "age":21,
    "city":"pune",
    "candrive":True,
    "city":"nagpur"
}

print(dict2)

for property in dict2:
    print(property,dict2[property])


a = [11,22,33]
b = a
b[0] = 44
print(b)
print(a)

vehicle = {
        "color":"blue",
        "city":"pune",
        "regNo":1234
}
vehicle2=vehicle
vehicle2['color']= "violet"
print(vehicle)
print(vehicle2)
