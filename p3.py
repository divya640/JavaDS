a,b=input().split()
a=int(a)
b=int(b)
arr=list(map(int,input().split()))
c=int(input())
arr.pop(b)
j=int(sum(arr)/2)
if(c==j):
    print("Bon Appetit")
else:
    print(c-j)

