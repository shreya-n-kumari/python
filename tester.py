from collections import Counter
shoes = int(input())
for _ in range(int(input('how many sizes want to enter'))): 
    sizes = Counter(map(int, input('enter sizes : ').split()))
customers = int(input('enter total customers'))
income = 0
for cust in range(customers):
    size = map(int, input('enter size').split())
    price = map(int, input('enter price').split())
    
    if sizes[size]:
        income = income + price
        sizes[size] -= 1
    else:
        pass   
print(income)