a,b=input().split()
a=int(a)
b=int(b)
d=100000007
count=0
p=1
for i in range(2,a+1):
   
    if(p-i!=b):
        count+=1
        p=i
    p=i
    print(i,p)
print(count%d)