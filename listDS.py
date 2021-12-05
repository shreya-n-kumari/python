monthly_exp = [2200,2350,2600,2130, 2190]


#In Feb, how many dollars you spent extra compare to January?
print("extra dollar spend than january in feb are : ", monthly_exp[1]- monthly_exp[0])

#Find out your total expense in first quarter (first three months) of the year.
print("Total expense in first quarter", monthly_exp[0]+ monthly_exp[1]+monthly_exp[2])

#Find out if you spent exactly 2000 dollars in any month.
print("2000$ in any month?",2000 in monthly_exp)

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
monthly_exp.append(1980)
print("expense after finish june month", monthly_exp)

"""You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""
monthly_exp[3] = monthly_exp[3] + 200
print("After refund", monthly_exp[3])