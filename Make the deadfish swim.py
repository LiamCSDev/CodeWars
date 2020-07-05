def parse(data):
    x = 0
    arr = []
    for c in data:
        if c == 'i': 
            x += 1
        elif c == 'd':
            x -=1
        elif c == 's':
            x *= x
        elif c == 'o':
            arr.append(x)
        else:
            continue
    return arr


print(parse("ooo")) 
print([0,0,0])
print(parse("ioioio"))
print([1,2,3])
print(parse("idoiido")) 
print([0,1])
print(parse("isoisoiso"))
print([1,4,25])
print(parse("codewars")) 
print([0])