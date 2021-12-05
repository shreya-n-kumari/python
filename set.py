s1 = set([1,2,3,4,5,6,8])
print(s1)
s2 = set([1,2,2,3,4,5,4,6,8,8])
print(s2)
s3 = set([3,4,6,8,8,6,2,1,1,1,1,1])
print(s3)

#we can pass in a list to initialize a set as in above code.

s4 = {"orange","apple","banana"}
print(s4)

s4.add('pineapple')
print(s4)

print("\nImplementing set operation")
s5 = {1,2,3,4}
s6 = {3,4,5,6}

print(s5 | s6)
print(s5.union(s6))

#using the & operator and intersection method for an intersection operation.
print(s5 & s6)
print(s5.intersection(s6))

#Use the – operator or the difference method to find the difference between two sets.
print(s5-s6)
print(s5.difference(s6))

#Now enter the <= operator or the issubset method to check if one set is a subset of another.
print(s5 <= s6)
print(s5.issubset(s6))

s7 = {1,2,3}
s8 = {1,2,3,4,5,6}

print(s7 <= s8)
print(s7.issubset(s8))

print("\n")
print(s7 < s8) #checking if s7 is formal subset of s8.

s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9)

print("\n")
print(s8 > s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)