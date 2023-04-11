def lcheck(a):
    ltr=len(a)
    if ltr<=200:
        return a
    else:
        k=a[0:200]
        return k
M=input()
print(lcheck(M))  
