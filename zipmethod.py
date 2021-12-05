items = ['apple','banana','cherry']
quantity = [2,5,8]

orders = zip(items,quantity) #zip function to combine two list into a tuple.
print(orders)

print(list(orders))  #convert zip object into a list.

orders = zip(items,quantity) 
print(orders)
print(tuple(orders)) #convert zip object into a tuple.

orders = zip(items,quantity) 
print(orders)
print(dict(orders))  #convert zip object into a dictionary.

