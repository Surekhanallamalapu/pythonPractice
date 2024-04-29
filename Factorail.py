def factorial(num):
    if type(num)!= int:
        return None
    if num < 0:
        return  None
    if num == 0:
        return 1
        
    # fact=1

    # i=1
    
    # while i<=num:
        
    #       fact = fact*i
        
    #       i= i+1
    # return fact
    return num * factorial(num-1)
factorial(5)