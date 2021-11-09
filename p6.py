a=int(input())
arr=[]
for i in range(a):
    arr.append(input())
for i in range(len(arr)):
    s1 = ""
    s2 = ""
    for j in range(len(arr[i])):    
        if j%2==0:
            s1+=arr[i][j]
        else:
            s2+=arr[i][j]
    print(s1+" "+s2)
