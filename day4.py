#program 1

firstName = "nilesh"
print(type(firstName))

lastName ='aher'
print(lastName)

city='pune'
print(city[0])
print(city[2])

# String
# properties
# methods

city="mumbai"
a=len(city)
print(a)
print(type(a))

#method

#program
city2 = "Nagpur"
q1  = city2.upper()
print(q1)
print(type(q1))

city3 = "MUMBAI"
q2 = city3.lower()
print(q2)
print(type(q2))

city4 = "chandrapuraa"
q3 = city4.count('a')
print(q3)
print(type(q3))

# Method chaining
z1=city4.upper().lower().count('a')
print(z1)

#program 3
city5='delhi'
q5 = city5.startswith("d")
q6 = city5.startswith("de")
print(q5)
print(q6)

#program 4
city6="pune"
q7 = city6.endswith('e')
q8 = city6.endswith('ne')
print(q7)
print(q8)
