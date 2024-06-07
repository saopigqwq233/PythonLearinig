n,v = input().split()
n = int(n)
v = int(v)

arr = []

for i in range(0,n):
    arr[i] = int(input())

if v in arr:
    print(arr.index(v))

