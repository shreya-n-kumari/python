#while loop....
i = 1
while i < 6 :
  print(i)
  i += 1  #NO SPACE BETWEEN + AND =
print("\n")


i = 1
while i < 6:
  print(i)
  print("\n")
  if i == 3:
     break    #break statement stop the loop when i equal to 3
  i += 1
  
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue  #continue to the next iteration when i = 3
  print(i)

  

  #print message once the condition false
  i = 1
  while i < 6:
    print(i)
    i+=1
  else :
    print("\ni is no longer less than 6")
#while loop....
i = 1
while i < 6 :
  print(i)
  i += 1  #NO SPACE BETWEEN + AND =
print("\n")


i = 1
while i < 6:
  print(i)
  print("\n")
  if i == 3:
     break    #break statement stop the loop when i equal to 3
  i += 1
  
"""i = 0
while i < 6:
  i += 1 
  if i == 3: code isn't working
    continue  #continue to the next iteration when i = 3
  print(i)"""

  

  #print message once the condition false
i = 1
while i < 6:
    print(i)
    i+=1
else:
  print("i is no longer less than 6")
  print("\n")

#for loop in python.........
print(">>>>>for loop output>>>>>>\n")

fruits = ["apple", "banana", "cherry"]    #list are written in square bracket.
for x in fruits:
  print(x)

for x in "banana":  #it'll print all element if banana one bt one
  print(x)

#break in for loop.
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in fruits:
  if x == "banana": 
    break
  print("--->" + x)
  print("\n")

for x in fruits:
    if x == "banana":
     continue
    print(x)

#range function..
for x in range(6):
 print(x)

print("--------")

for x in range(2,6):
  print(x)

print("---------------")

for x in range(2,30,3):
  print(x)

print("-----------------")

for x in range(6):
  print(x)
else:
  print("FINISHED!\n")

print(">>nested for loop>>")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana","cherry"]
for x in adj:
  for y in fruits:
    print(x,y)

