def catch_sign_change(lst):
    count = 0
    positive = False

    if lst and lst[0] < 0:
        positive = True
    
    for v in lst: 
        if v >= 0 and positive or v < 0 and not positive:
           count += 1
           positive = not positive
        
    return count

print(catch_sign_change([1, 3, 4, 5]))
#0
print(catch_sign_change([1, -3, -4, 0, 5]))
#2
print(catch_sign_change([]))
#0
print(catch_sign_change([-47,84,-30,-11,-5,74,77]))
#3
