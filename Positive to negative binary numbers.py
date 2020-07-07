#Getting the two's complement negative notation of an integer
def positive_to_negative(binary):
    #Invert the binary values
    negativeBinary = []
    for index in binary:
        if index == 0:
            negativeBinary.append(1)
        else: 
            negativeBinary.append(0)

    #Add one to the binary value
    result = []
    addedOne = False
    for x, e in reversed(list(enumerate(negativeBinary))):
        if negativeBinary[x] == 0 and not addedOne:
            negativeBinary[x] = 1
            addedOne = True
        elif not addedOne:
           negativeBinary[x] = 0

    return negativeBinary

print(positive_to_negative([1, 0, 1, 1]))