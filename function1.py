#Defining and Calling the Function in Python Script.
def list_product(my_list): 
    result = 1
    for number in my_list: 
         result = result * number
    return result

print(list_product([2, 3]))
print(list_product([2, 10, 15]))



def add_suffix(suffix = '.com'):
	return 'google' + suffix

print(add_suffix())					#without specifying argument(default argument).
print(add_suffix('.nic.in'))		#with argument.