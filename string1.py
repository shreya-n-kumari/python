def count_substring(string, sub_string):

	res=0
	for i in range(0,len(string)):
		if (i+len(sub_string)) > len(string) :
			break
		if string[i: (i+len(sub_string))].find(sub_string) != -1:
			res+=1
	return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)