n=int(input())
a=int(input())
b=int(input())
def simple_arithmetic(n,a,b):
    if n==1:
        return(a+b)
    elif n==2:
        return(a-b)
    elif n==3:
        return(a*b)
    elif n==4:
        return(a/b)
    elif n==5:
        return(a%b)
    elif n==6:
        return(a//b)
    elif n==7:
        return(a**b)
    else:
        return('Invalid Input')
print(simple_arithmetic(n,a,b))
