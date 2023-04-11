def hotel_exp(room_type,days,food_price):
    if room_type == 'Delux room':
        a = 7500*days
        print('price_of_stay:',a)
        sgst = 0.09*food_price
        cgst = 0.09*food_price
        tip = 0.1*food_price
        print('SGST:', round(sgst, 2)) 
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', c+sgst+cgst+tip)
        
    elif room_type=='Non AC Room':
        a = 4500 * days
        print('price_of_stay:', a)
        sgst = 0.025 * food_price
        cgst = 0.025 * food_price
        tip = 0.1 * food_price
        print('SGST:', round(sgst, 2))
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', c+sgst+cgst+tip)
    else:
        print('Invalid room type')
a = input('Type of room: ') 
b = int(input('Number of days you stayed: ')) 
c = int(input('Total food amount: ')) 

hotel_exp(a,b,c)
