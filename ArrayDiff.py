def array_diff(a, b): 
    for num in b:
        if num in a: 
            while num in a: 
                a.remove(num)
    return a

print(array_diff([1,2], [1]) == [2])
print(array_diff([1,2,2], [1]) == [2,2])
print(array_diff([1,2,2], [2]) == [1])
print(array_diff([1,2,2], []) == [1,2,2])
print(array_diff([], [1,2]) == [])
