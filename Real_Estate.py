print('A one bedroom in the bay area is listed at Rs.1000000')
print('Enter your first offer on the house')
offer = abs(int(input()))
print('Enter your best offer on the house.')
best = abs(int(input()))
print('How much time you want to offer each time?')
increment = abs(int(input()))
offer_accepted = False
print('----before while')
while offer <= best:
	if offer >= 650000:
		print('-----after if')
		offer_accepted = True
		print('Your offer of',offer,'has been accepted!')
		break
		print('.........')
	
	print('we\'re sorry,your offer of Rs.',offer,'has not been accepted')
	offer =+ increment	

