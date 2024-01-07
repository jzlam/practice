def isHappy(n): 
    sum = 0 
    if sum == 0: 
        return False 
    while sum != 1 or sum != 4: 
        while n > 0 : 
            digit = n % 10 
            
            sum += digit ** 2 
            print(digit, sum)
            n //= 10
        n = sum 
    
    if sum == 1: 
        return True 
    else: 
        return False 

print(isHappy(7)) 