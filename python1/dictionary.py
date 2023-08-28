students  = ['nil','ram','sanjeev','raj']
marks = [65,64,61,32]

print(type(students))

# var_name = {key1: value1,key2:value2 }

students1={
    'nil':32,
    'ram':66,
    'sanjay':13,
    'raj':89
}
print(students1)
print(type(students1))


student2 = {} #creating an empty Dictionary
print(type(student2))


# accessing the Dictionary using []
print(students1['nil'])
print(students1['ram'])

#dot notation
print(students1.get('raj'))