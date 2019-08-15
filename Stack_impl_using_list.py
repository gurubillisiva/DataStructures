def push(elmnt):
    stack.append(elmnt)
    
def pop():
    if len(stack)!=0:
        x=stack.pop()
        print("Element poped was ",x)
    else:
        print("stack is empty")
    
def display():
    print("===========================================")
    print("Elements are ", stack, "Stack length",len(stack))
    print("===========================================")
    

print("Stack implementation in Python using List")
stack=[]
ch=0
while(ch!=3):
    print("1. Push 2. Pop 3. Exit\nEnter your choice")
    y=input()
    if y.isdigit():
        ch=int(y)
        
        if ch==1:
            elemnt=int(input("Enter a value to push into stack"))
            push(elemnt)
            display()
        elif ch==2:
            pop()
            display()
        elif ch==3:
            break
        else:
            print("Invalid choice")
    
    else:
        print("Invalid-Not a number")
    

