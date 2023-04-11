price=float(input("Price: "))
a=input("Are you prime member? " )
def dscnt_p(price, a):
    if (a=="yes" or a=="Yes"):
        disco_1 = 0.15*price
        p_d1= price-disco_1
        disco_2= 0.08*p_d1
        p_d2=p_d1-disco_2
        return p_a_d2
    else:
        bfd=0.08*price
        fp= price-bfd
        return fp
print("Your final price after calculating all discounts is Rs",dscnt_p(price,a))
