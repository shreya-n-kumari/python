X = int(input("Enter a Year"))
result = "Leap Year" if X%400 == 0 else "Leap Year" if X%4 == 0 and X%100 != 0 else "Not a Leap Year"
print(result)