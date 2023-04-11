s=int(input())
def cat_prsn_age(s):
    if s==1:
        return(s,15)
    elif s==2:
        return(s,24)
    elif s>2:
        h=24+4*(s-2)
        return(s,h)
        s+=1
print(cat_prsn_age(s))
