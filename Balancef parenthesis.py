open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                print("Unbalanced")
    if len(stack) == 0: 
        print("Balanced")
    else:
        return "NO"
  
# Driver code 
t=int(input())
for i in range(t):
    string = input()
    print(check(string))
