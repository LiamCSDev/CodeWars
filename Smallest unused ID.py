def next_id(arr):
    if len(arr) == 0 :
        return 0
    else:
        arr.sort()
        lowestID = 0
        for value in arr:
          if value <= lowestID:
              lowestID = value + 1

        return lowestID

#Better Approach 
def next_id_improved(arr):    
    availableID = 0
    while availableID in arr:
        availableID +=1
    return t

print(next_id([0,1,2,3,5]))
print(next_id([0,1,0,3,5]))
print(next_id([0]))
print(next_id([]))
