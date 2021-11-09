from collections import Counter
a=int(input())
arr = list(map(int, input().split()))
result=Counter(arr)

r=list(result.values())
count=0   
for i in result.keys():
    
    if(i>0):
    
        count=count+int(result[i]/2)
    
# #     if result[i]== max(r):
# #          a.append(i)

print(count)