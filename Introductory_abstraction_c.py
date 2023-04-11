magnitude = float(input("Enter earthquake magnitude: "))
def erthqke_msrmnt(magnitude):
    if magnitude < 2.0:
        return("Micro earthquake")
    elif magnitude >= 2.0 and magnitude < 3.0:
        return(" Very Minor earthquake")
    elif magnitude >= 3.0 and magnitude < 4.0:
        return("Minor earthquake")
    elif magnitude >= 4.0 and magnitude < 5.0:
        return("Light earthquake")
    elif magnitude >= 5.0 and magnitude < 6.0:
        return("Moderate earthquake")
    elif magnitude >= 6.0 and magnitude < 7:
        return("Strong earthquake")
    elif magnitude >= 7.0 and magnitude < 8:
        return("Major earthquake")
    elif magnitude >= 8.0 and magnitude < 10:
        return('Great earthquake')
erthqke_msrmnt(magnitude)
