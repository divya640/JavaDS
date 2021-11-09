
a={}
ar=int(input())
li=[]


for i in range(ar):
     c,d=input().split()
     d=int(d)
     a[c.lower()]=d
while True:
    try:
        s=input()
        if s in a.keys():
            print(s+"="+str(a[s]))
        else:
            print("Not found")     
    except EOFError:
        break



