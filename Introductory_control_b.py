num=int(input())
def sum_of_divisors(num):          
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum

def category_check(num):            
    div_sum = sum_of_divisors(num)
    if div_sum > num:
        return "abundant"
    elif div_sum < num:
        return "deficient"
    else:
        return "perfect"

for num in range(1, num):
    category = category_check(num)
    print(f"{num}: {category}")
