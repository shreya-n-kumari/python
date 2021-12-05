n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    choice = input().split()
    if choice == 'pop':
        print(s.pop())
    elif choice == 'remove':
        s.remove()
    elif choice == 'discard':
        s.discard()
print(sum(s))