movie = {"title": "padmavati", "director": "Bhansali","year": "2018", "rating": "4.5"}
print(movie)
print(movie['year'])

movie['year'] = 2019  #update data.
print(movie['year'])
print('-' * 20)

for x in movie:
	print(x)            #this print key.
	print(movie[x])     #this print value at key.
	print('-' * 20)


movie = {}
movie['title'] = 'Manikarnika'
movie['Director'] = 'kangana Ranut'
movie['year'] = '2015'
print(movie)



movie['actor'] = ['kangana Ranut', 'Khilge','Pelge']               #defining a list within dictionary.
movie['other_detail'] = {'language': 'Hindi', 'runtime': '180min'} #defining a dictinary witnin dictionay.
print(movie)

print('\n...........new example........')
orders = {'apple': 2, 'banana': 5 , 'orange': 10}
print(orders.values())
print(list(orders))
print(list(orders.values()))

for tuple in list(orders.items()): #iterate in dictionary , converting in tuple by using items() method.
	print(tuple)