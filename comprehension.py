l = [x for x in range(0,10)]
s = {x for x in range(0,10)}
t = tuple(x for x in range(0,10))	#it will give error  if tuple keyword not used...
d = {x : x*x for x in range(0,10)}


print(l)
print(s)
print(t)
print(d)