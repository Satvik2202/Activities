#Cat to human age convertor

s=int(input())

if s==1:
     print(s,15)
elif s==2:
     print(s,24)
elif s>2:
    h=24+4*(s-2)
    print(s,h)
    s+=1
