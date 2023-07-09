def push(stack,item):
    stack.append(item)
def isempty(stack):
    return len(stack)==0
def pop(stack):
    if isempty(stack):
        print("stack is already empty")
    return stack.pop()
def reverse(str):
    size=len(str)
    stack=[]
    for i in range(size):
        push(stack,str[i])
    str=" "
    for i in range(size):
        str+=pop(stack)
    return str

if __name__=="__main__":
    str=str(input('enter the string ='))
    print("the reverse string =",reverse(str))