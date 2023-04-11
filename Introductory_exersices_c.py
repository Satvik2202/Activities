magnitude = float(input("Enter earthquake magnitude: "))

if magnitude < 2.0:
    print("Micro earthquake")
elif magnitude >= 2.0 and magnitude < 3.0:
    print(" Very Minor earthquake")
elif magnitude >= 3.0 and magnitude < 4.0:
    print("Minor earthquake")
elif magnitude >= 4.0 and magnitude < 5.0:
    print("Light earthquake")
elif magnitude >= 5.0 and magnitude < 6.0:
    print("Moderate earthquake")
elif magnitude >= 6.0 and magnitude < 7:
    print("Strong earthquake")
elif magnitude >= 7.0 and magnitude < 8:
    print("Major earthquake")
elif magnitude >= 8.0 and magnitude < 10:
    print('Great earthquake')
