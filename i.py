def isBalanced(s):
    open = ["[","{","("] 
    close = ["]","}",")"] 
  
# Function to check parentheses 
# Driver code 

    stack = [] 
    for i in s:
        if i in open: 
            stack.append(i) 
        elif i in close: 
            pos = close.index(i) 
            if ((len(stack) > 0) and
                (open[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "NO"
    if len(stack) == 0: 
       return "YES"
    else:
        return "NO"
s=input()
result=isBalanced(s)
print(result)
  

