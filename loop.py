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
     break		#break statement stop the loop when i equal to 3
  i += 1
  
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue	#continue to the next iteration when i = 3
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
     break		#break statement stop the loop when i equal to 3
  i += 1
  
"""i = 0
while i < 6:
  i += 1 
  if i == 3: code isn't working
    continue	#continue to the next iteration when i = 3
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
fruits = ["apple", "banana", "cherry"]    #list are written in square bracket.
for x in fruits:
	print(x)

for x in "banana":
	print(x)

#break in for loop.
for x in fruits:
	print(x)
	if x == "banana":
		break

for x in fruits:
	if x == "banana":
		break
		print(x)
