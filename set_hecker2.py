A = set(input().split())
n = int(input())
for i in range(n):
    N = set(input().split())
    z = A.issuperset(N)
print(z)
