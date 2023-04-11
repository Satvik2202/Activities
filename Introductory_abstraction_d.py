def wind_chill(temp_c, wind_sp):
    change= 13.12 + 0.6215*temp_c - 11.37*(wind_sp**0.16) + 0.3965*temp_c*(wind_sp**0.16)
    return change
T=float(input())
V=float(input())
print(round(wind_chill(T,V),4),'°C')
