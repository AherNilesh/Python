#set
list_num = [11,22,33,44,55]
print(list_num[4])
print(list_num[2])

# using range() in for loop

for i in range(0,11):
  print(i)

for i in range(5, 51, 5):
    print(i)

# empty set is a dictionary

s1 = {11,22,33,44}
print(s1)
print(type(s1))

# duplicates are not allowed
s2 = {11,11,22,22,33,33,44,44}
print(s2)
print(type(s2))

s5 = {22}
print(type(s5))
#dict
s5 = {}
print(type(s5))


a1 = set() #to make an empty set using constructor
print(a1)
print(type(a1))