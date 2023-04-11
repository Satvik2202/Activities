temp_C=float(input())
wind_spd=float(input())
wind_chill= 13.12 + 0.6215*temp_C - 11.37*(wind_spd**0.16) + 0.3965*temp_C*(wind_spd**0.16)
print(round(wind_chill,4),"°C")
