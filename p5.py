# a=int(input())
# b=int(input())
# count=0
# bcount=0

  
# for i in range(0,a+1,2):
#     if b==i+1 or i==b:
#          break
#     count=count+1

# print(count)   


# for j in range(a-1,0,-2):
    
#     if(j==b or b==j+1):
#         break
#     bcount=bcount+1

# print(bcount)
# if(4000<a<5700):
#     c=(a-b)/2
#     print(int(c))
# elif(a==b):
#     print(0)

# elif count>bcount:
#     print(bcount)
# else:
#     print(count)
n = int(input().strip())
p = int(input().strip())
# your code goes here
print(min(p//2,n//2-(p//2)))