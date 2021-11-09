from collections import Counter
a=int(input())
arr = list(map(int, input().split()))
arr.sort()
count=0
a=[]
result=Counter(arr)
r=list(result.values())
print(r)
for i in result.keys():
    if result[i]== max(r):
         a.append(i)

print(min(a))