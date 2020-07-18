def solve(arr):
    arr.sort()
    if arr[0] + arr[1] < arr[2]: 
        return arr[0] + arr[1]
    else :
        return int((int(arr[0]) + int(arr[1]) + int(arr[2])) / 2)

print(solve([1,1,1]) == 1)
print(solve([1,2,1]) == 2)
print(solve([4,1,1]) == 2)
print(solve([8,2,8]) == 9)
print(solve([8,1,4]) == 5)
print(solve([7,4,10]) == 10) 
print(solve([12,12,12]) == 18) 
print(solve([1,23,2]) == 3)