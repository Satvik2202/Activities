wavelength=int(input())
if wavelength in range(380,450):
    print('Violet')
elif wavelength in range(450,495):
    print('Blue')
elif wavelength in range(495,570):
    print('Green')
elif wavelength in range(570,590):
    print('Yellow')
elif wavelength in range(590,620):
    print('Orange')
elif wavelength in range(620,750):
    print('Red')
else:
    print('Invalid Range Input')

