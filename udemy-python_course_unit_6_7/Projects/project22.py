def factorial(fac_num):
 
    returned = 1
    
    for item in range(fac_num, 1, -1):
        returned *= item
 
    
    return returned
 
 
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120