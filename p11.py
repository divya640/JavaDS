a,b=input().split()
a=int(a)
b=int(b)
arr=list(map(int,input().split()))
for i in range(b):
  
     m=arr[b]
     arr[b]=arr[i]
     arr[i]=m
     if(b<a-1):
          b+=1
     else:
        pass

        
    
for i in arr:
    print(i,end=" ")