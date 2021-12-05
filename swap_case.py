def swap_case(s):
    result = s.swapcase()
   # print(result)
    """length = len(s)
    print(length)
    for i in range(0,length):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            c = (s[i].lower())
            #print(c)
        elif (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            c = (s[i].upper())
            #print(c)"""
    return result

if __name__ == '__main__':
    s = input()
    print("Accepted input : ", s)
    result = swap_case(s)
    print(result)
