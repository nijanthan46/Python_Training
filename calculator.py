print("========calculation========")
print("Addition(+)")
print("Subtraction(-)")
print("Multiplication(*)")
print("Division(/)")
def calculation(a,b,c):
    if choice=='+':
        return a+b
    elif choice=='-':
        return a-b
    elif choice=='*':
        return a*b
    elif choice=='/':
        if b==0:
            print("division zero not allowed")
        else:
            return a/b
    elif choice=='%':
        return("invalid")
num1=int(input("Enter the first value="))
num2=int(input("Enter the second value="))
choice=input("Enter the choice(+/-/*///%)")
result = calculation(num1,num2,choice)
print("result",result)
    
          