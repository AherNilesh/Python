# Set in Python

set={2,4,6,8,10}
set.add(12)
print(set)
print(type(set))

set_fruits = {'apple','mango','banana'}
set_fruits.add('kiwi')
print(set_fruits)

set_fruits.add(22)
print(set_fruits)

# duplicates are not allowed
set_fruits.add('banana')
print(set_fruits)

# set operations
set1 = {0,2,4,6,8,10}
set2 = {0,1,3,5,7,9}
print(set1.union(set2))
print(set2.intersection(set1)) #same
print(set2.intersection_update(set1))
print(set2.difference(set1))


# boolean outputs
set_a = {1,2,3,4,5,6,7,8,9}
set_b = {2,4,6,8}
set_c = {0}

print(set_b.issubset(set_a))
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))

print(set_a.isdisjoint(set_b))
print(set_b.isdisjoint(set_a))

print(set_b.isdisjoint(set_c))
print(set_c.isdisjoint(set_a))

set4 ={0,1,2,3,4,5,6,7,8,9}
print(set4.pop())
print(set4.pop())
print(set4.pop())
print(set4.pop())
print(set4)

set5={0,1,2,3,4,5,6,7,8,9}
set5.remove(7)
print(set5)

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {2,4,6,8}
set3 = {0}
print(set2.issubset(set1))

if set3.issubset(set1):
  print("set 2 is Subset of set 1")
else:
  print("Not a subset ")
